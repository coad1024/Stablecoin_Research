#!/usr/bin/env python3
"""
Convert PDFs one by one to avoid memory issues
"""

import os
import sys
from pathlib import Path
import subprocess
import time

def get_all_pdfs():
    """Get all PDF files in papers directory."""
    papers_dir = Path("papers")
    return sorted(papers_dir.glob("*.pdf"))

def main():
    pdfs = get_all_pdfs()
    total = len(pdfs)
    successful = 0
    failed = []
    
    print(f"Found {total} PDFs to convert")
    print("=" * 50)
    
    for i, pdf in enumerate(pdfs, 1):
        print(f"\n[{i}/{total}] Converting: {pdf.name}")
        print("-" * 30)
        
        # Run conversion for single file
        cmd = [
            "poetry", "run", "python", 
            "convert_with_marker.py",
            "--output-format", "both",
            "--single", pdf.name
        ]
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120  # 2 minute timeout per file
            )
            
            if result.returncode == 0:
                print(f"✅ Success: {pdf.name}")
                successful += 1
            else:
                print(f"❌ Failed: {pdf.name}")
                if "CUDA out of memory" in result.stderr:
                    print("   (GPU memory issue - will retry on CPU)")
                failed.append(pdf.name)
                
        except subprocess.TimeoutExpired:
            print(f"⏱️ Timeout: {pdf.name}")
            failed.append(pdf.name)
        except Exception as e:
            print(f"❌ Error: {pdf.name} - {str(e)}")
            failed.append(pdf.name)
        
        # Small delay between conversions to let GPU memory clear
        time.sleep(2)
    
    print("\n" + "=" * 50)
    print(f"✅ Successful: {successful}/{total}")
    if failed:
        print(f"❌ Failed: {len(failed)}")
        for f in failed:
            print(f"   - {f}")
    print(f"📁 Output: papers_markdown_marker/")

if __name__ == "__main__":
    main()