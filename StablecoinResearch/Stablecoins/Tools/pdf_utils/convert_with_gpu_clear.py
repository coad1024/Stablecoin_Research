#!/usr/bin/env python3
"""
Convert PDFs with aggressive GPU memory clearing
"""

import os
import sys
from pathlib import Path
import subprocess
import time
import gc

def clear_gpu_memory():
    """Aggressively clear GPU memory."""
    try:
        import torch
        if torch.cuda.is_available():
            # Clear PyTorch's cache
            torch.cuda.empty_cache()
            torch.cuda.synchronize()
            
            # Reset max memory stats
            torch.cuda.reset_peak_memory_stats()
            torch.cuda.reset_accumulated_memory_stats()
            
            print("  → GPU memory cleared")
    except:
        pass
    
    # Force Python garbage collection
    gc.collect()

def convert_single_pdf_subprocess(pdf_path):
    """Run conversion in a subprocess to ensure complete memory cleanup."""
    cmd = [
        "python", "-c",
        f"""
import os
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True,max_split_size_mb:128'
from pathlib import Path
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
import torch
import gc

pdf_path = Path('{pdf_path}')
output_dir = Path('papers_markdown_marker')

try:
    # Create converter
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
        config={{"output_format": "markdown"}}
    )
    
    # Convert
    rendered = converter(str(pdf_path))
    text, metadata, images = text_from_rendered(rendered)
    
    # Save markdown
    md_path = output_dir / f"{{pdf_path.stem}}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print("SUCCESS")
    
except Exception as e:
    print(f"ERROR: {{str(e)[:100]}}")
finally:
    # Cleanup
    if 'converter' in locals():
        del converter
    if 'rendered' in locals():
        del rendered
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
"""
    ]
    
    env = os.environ.copy()
    env['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True,max_split_size_mb:128'
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120,
            env=env
        )
        
        if "SUCCESS" in result.stdout:
            return True, "✅ Converted successfully"
        else:
            error_msg = result.stdout + result.stderr
            if "CUDA out of memory" in error_msg:
                return False, "❌ GPU memory error"
            else:
                return False, f"❌ {error_msg[:100]}"
    except subprocess.TimeoutExpired:
        return False, "⏱️ Timeout"
    except Exception as e:
        return False, f"❌ {str(e)[:100]}"

def main():
    """Convert PDFs with aggressive memory management."""
    papers_dir = Path("papers")
    output_dir = Path("papers_markdown_marker")
    output_dir.mkdir(exist_ok=True)
    
    # Find missing PDFs
    missing = []
    for pdf in sorted(papers_dir.glob("*.pdf")):
        if not (output_dir / f"{pdf.stem}.md").exists():
            missing.append(pdf)
    
    print(f"Found {len(missing)} PDFs to convert")
    print("Using subprocess isolation for memory management")
    print("=" * 50)
    
    successful = 0
    failed = []
    
    # Clear memory before starting
    clear_gpu_memory()
    
    for i, pdf in enumerate(missing, 1):
        print(f"\n[{i}/{len(missing)}] {pdf.name}")
        
        # Clear memory before each conversion
        clear_gpu_memory()
        time.sleep(2)  # Give GPU time to release memory
        
        # Run conversion in subprocess for complete isolation
        success, msg = convert_single_pdf_subprocess(pdf)
        print(f"  {msg}")
        
        if success:
            successful += 1
        else:
            failed.append(pdf.name)
        
        # Clear memory after conversion
        clear_gpu_memory()
        
        # Longer wait between conversions
        time.sleep(5)
    
    print("\n" + "=" * 50)
    print(f"✅ Successful: {successful}/{len(missing)}")
    if failed:
        print(f"❌ Failed: {len(failed)}")
        for f in failed:
            print(f"   - {f}")

if __name__ == "__main__":
    # Set optimal GPU memory configuration
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True,max_split_size_mb:128"
    main()