#!/usr/bin/env python3
"""
Convert PDFs with GPU memory cleanup between each conversion
"""

import os
import sys
from pathlib import Path
import subprocess
import time
import gc

def clear_gpu_memory():
    """Aggressively clear GPU memory and kill Python processes."""
    try:
        import torch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.synchronize()
            print("  → GPU cache cleared")
    except:
        pass
    
    # Force garbage collection
    for _ in range(3):
        gc.collect()

def convert_single_pdf_isolated(pdf_name):
    """Run conversion in complete isolation and kill process after."""
    cmd = [
        "timeout", "300",  # 5 minute timeout
        "poetry", "run", "python", 
        "convert_with_marker.py",
        "--single", pdf_name,
        "--output-format", "markdown"
    ]
    
    env = os.environ.copy()
    env['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            env=env
        )
        
        # Check if file was created
        output_dir = Path("papers_markdown_marker")
        pdf_stem = Path(pdf_name).stem
        md_file = output_dir / f"{pdf_stem}.md"
        
        if md_file.exists():
            return True, f"✅ {pdf_name}"
        else:
            if "CUDA out of memory" in result.stderr:
                return False, f"❌ {pdf_name}: GPU memory issue"
            else:
                return False, f"❌ {pdf_name}: Conversion failed"
    except Exception as e:
        return False, f"❌ {pdf_name}: {str(e)[:50]}"

def main():
    """Convert PDFs with aggressive cleanup between each."""
    papers_dir = Path("papers")
    output_dir = Path("papers_markdown_marker")
    output_dir.mkdir(exist_ok=True)
    
    # Find missing PDFs
    missing = []
    for pdf in sorted(papers_dir.glob("*.pdf")):
        if not (output_dir / f"{pdf.stem}.md").exists():
            missing.append(pdf)
    
    if not missing:
        print("All PDFs have been converted!")
        return
    
    print(f"Found {len(missing)} PDFs to convert")
    print("Will clear GPU memory between each conversion")
    print("=" * 50)
    
    successful = 0
    failed = []
    
    for i, pdf in enumerate(missing, 1):
        print(f"\n[{i}/{len(missing)}] Converting: {pdf.name}")
        
        # Clear memory before conversion
        clear_gpu_memory()
        time.sleep(3)
        
        # Convert with isolation
        success, msg = convert_single_pdf_isolated(pdf.name)
        print(f"  {msg}")
        
        if success:
            successful += 1
        else:
            failed.append(pdf.name)
        
        # Clear memory after conversion
        clear_gpu_memory()
        
        # Kill any lingering Python processes that might hold GPU memory
        # (This is aggressive but safe since we're between conversions)
        subprocess.run(
            ["pkill", "-f", "marker.*convert"],
            capture_output=True
        )
        
        # Wait before next conversion
        print("  → Waiting for GPU memory to clear...")
        time.sleep(5)
    
    print("\n" + "=" * 50)
    print(f"✅ Successful: {successful}/{len(missing)}")
    if failed:
        print(f"❌ Failed: {len(failed)}")
        for f in failed[:5]:  # Show first 5 failures
            print(f"   - {f}")
        if len(failed) > 5:
            print(f"   ... and {len(failed)-5} more")

if __name__ == "__main__":
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    main()