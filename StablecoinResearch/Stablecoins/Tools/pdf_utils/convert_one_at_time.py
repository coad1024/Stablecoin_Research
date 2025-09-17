#!/usr/bin/env python3
"""
Convert PDFs one at a time, handling failures gracefully
"""

import os
import sys
from pathlib import Path
import subprocess
import time

def convert_single_pdf(pdf_name):
    """Convert a single PDF, return success status."""
    cmd = [
        "poetry", "run", "python", 
        "convert_with_marker.py",
        "--single", pdf_name,
        "--output-format", "markdown"
    ]
    
    env = os.environ.copy()
    env['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'
    
    try:
        print(f"  Starting conversion...")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout
            env=env
        )
        
        # Check if file was actually created
        output_dir = Path("papers_markdown_marker")
        pdf_stem = Path(pdf_name).stem
        md_file = output_dir / f"{pdf_stem}.md"
        
        if md_file.exists():
            file_size = md_file.stat().st_size
            print(f"  ✅ SUCCESS - Created {md_file.name} ({file_size:,} bytes)")
            return True
        else:
            if "CUDA out of memory" in result.stderr:
                print(f"  ❌ FAILED - GPU memory error")
            else:
                print(f"  ❌ FAILED - Conversion error")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"  ⏱️ TIMEOUT - Took too long")
        return False
    except Exception as e:
        print(f"  ❌ ERROR - {str(e)[:100]}")
        return False

def main():
    """Convert all missing PDFs one at a time."""
    papers_dir = Path("papers")
    output_dir = Path("papers_markdown_marker")
    output_dir.mkdir(exist_ok=True)
    
    # Get all PDFs
    all_pdfs = sorted(papers_dir.glob("*.pdf"))
    
    # Find which ones are missing
    missing = []
    already_done = []
    for pdf in all_pdfs:
        md_file = output_dir / f"{pdf.stem}.md"
        if md_file.exists():
            already_done.append(pdf.name)
        else:
            missing.append(pdf)
    
    print(f"📊 Status:")
    print(f"  Total PDFs: {len(all_pdfs)}")
    print(f"  Already converted: {len(already_done)}")
    print(f"  Need to convert: {len(missing)}")
    
    if already_done:
        print(f"\n✅ Already converted:")
        for name in already_done[:5]:
            print(f"  - {name}")
        if len(already_done) > 5:
            print(f"  ... and {len(already_done)-5} more")
    
    if not missing:
        print("\n🎉 All PDFs have been converted!")
        return
    
    print(f"\n📝 Will attempt to convert {len(missing)} PDFs:")
    for pdf in missing[:5]:
        print(f"  - {pdf.name}")
    if len(missing) > 5:
        print(f"  ... and {len(missing)-5} more")
    
    print("\n" + "=" * 60)
    print("Starting conversions (will continue even if some fail)...")
    print("=" * 60)
    
    successful = []
    failed = []
    
    for i, pdf in enumerate(missing, 1):
        print(f"\n[{i}/{len(missing)}] Converting: {pdf.name}")
        
        success = convert_single_pdf(pdf.name)
        
        if success:
            successful.append(pdf.name)
        else:
            failed.append(pdf.name)
            print("  Continuing with next file...")
        
        # Small delay between conversions
        if i < len(missing):
            print("  Waiting 3 seconds before next conversion...")
            time.sleep(3)
    
    # Final summary
    print("\n" + "=" * 60)
    print("📊 FINAL SUMMARY")
    print("=" * 60)
    
    print(f"\n✅ Successfully converted: {len(successful)}/{len(missing)}")
    if successful:
        for name in successful:
            print(f"  - {name}")
    
    if failed:
        print(f"\n❌ Failed to convert: {len(failed)}/{len(missing)}")
        for name in failed:
            print(f"  - {name}")
    
    print(f"\n📁 Total files in output directory: {len(list(output_dir.glob('*.md')))}")
    print(f"📂 Output location: {output_dir.absolute()}")

if __name__ == "__main__":
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    main()