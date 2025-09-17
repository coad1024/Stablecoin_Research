#!/usr/bin/env python3
"""
Convert PDFs with reduced memory usage
"""

import os
import sys
from pathlib import Path
import time
import torch
import gc

def convert_with_low_memory(pdf_path, output_dir):
    """Convert a single PDF with aggressive memory management."""
    try:
        # Force garbage collection before starting
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        
        from marker.converters.pdf import PdfConverter
        from marker.models import create_model_dict
        from marker.output import text_from_rendered
        
        print(f"Converting: {pdf_path.name}")
        
        # Create converter with markdown-only output to save memory
        config = {"output_format": "markdown"}
        converter = PdfConverter(
            artifact_dict=create_model_dict(),
            config=config
        )
        
        # Convert the PDF
        rendered = converter(str(pdf_path))
        
        # Extract text
        text, metadata, images = text_from_rendered(rendered)
        
        # Save markdown
        md_path = output_dir / f"{pdf_path.stem}.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        # Clean up memory immediately
        del converter
        del rendered
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        
        return True, f"✅ {pdf_path.name}"
        
    except Exception as e:
        return False, f"❌ {pdf_path.name}: {str(e)[:100]}"

def main():
    """Convert missing PDFs with aggressive memory management."""
    papers_dir = Path("papers")
    output_dir = Path("papers_markdown_marker")
    output_dir.mkdir(exist_ok=True)
    
    # Find missing PDFs
    missing = []
    for pdf in sorted(papers_dir.glob("*.pdf")):
        if not (output_dir / f"{pdf.stem}.md").exists():
            missing.append(pdf)
    
    print(f"Found {len(missing)} PDFs to convert")
    print("=" * 50)
    
    successful = 0
    failed = []
    
    for i, pdf in enumerate(missing, 1):
        print(f"\n[{i}/{len(missing)}] {pdf.name}")
        
        success, msg = convert_with_low_memory(pdf, output_dir)
        print(msg)
        
        if success:
            successful += 1
        else:
            failed.append(pdf.name)
        
        # Wait between conversions to let memory clear
        time.sleep(3)
    
    print("\n" + "=" * 50)
    print(f"✅ Successful: {successful}/{len(missing)}")
    if failed:
        print(f"❌ Failed: {len(failed)}")
        for f in failed:
            print(f"   - {f}")

if __name__ == "__main__":
    # Set memory management environment variable
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    main()