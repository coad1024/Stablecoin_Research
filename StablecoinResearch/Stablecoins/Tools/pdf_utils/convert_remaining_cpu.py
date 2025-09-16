#!/usr/bin/env python3
"""
Convert remaining PDFs using CPU-only mode to avoid GPU memory issues
"""

import os
import sys
from pathlib import Path
import subprocess
import time

# Force CPU-only mode
os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["USE_CPU"] = "1"

def get_missing_pdfs():
    """Get PDFs that haven't been converted yet."""
    papers_dir = Path("papers")
    output_dir = Path("papers_markdown_marker")
    
    missing = []
    for pdf in sorted(papers_dir.glob("*.pdf")):
        md_file = output_dir / f"{pdf.stem}.md"
        if not md_file.exists():
            missing.append(pdf)
    return missing

def main():
    missing_pdfs = get_missing_pdfs()
    total = len(missing_pdfs)
    
    if total == 0:
        print("All PDFs have been converted!")
        return
    
    print(f"Found {total} PDFs that need conversion")
    print("Using CPU-only mode to avoid GPU memory issues")
    print("=" * 50)
    
    successful = 0
    failed = []
    
    for i, pdf in enumerate(missing_pdfs, 1):
        print(f"\n[{i}/{total}] Converting: {pdf.name}")
        print("-" * 30)
        
        # Run conversion with CPU-only environment
        cmd = [
            "poetry", "run", "python", 
            "convert_with_marker.py",
            "--output-format", "both",
            "--single", pdf.name
        ]
        
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = ""
        env["USE_CPU"] = "1"
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout for CPU mode
                env=env
            )
            
            # Check if files were actually created
            output_dir = Path("papers_markdown_marker")
            md_file = output_dir / f"{pdf.stem}.md"
            json_file = output_dir / f"{pdf.stem}.json"
            
            if md_file.exists() and json_file.exists():
                print(f"✅ Success: {pdf.name}")
                successful += 1
            else:
                print(f"❌ Failed to create files: {pdf.name}")
                failed.append(pdf.name)
                if result.stderr:
                    print(f"   Error: {result.stderr[:200]}")
                
        except subprocess.TimeoutExpired:
            print(f"⏱️ Timeout: {pdf.name} (CPU mode is slower)")
            failed.append(pdf.name)
        except Exception as e:
            print(f"❌ Error: {pdf.name} - {str(e)}")
            failed.append(pdf.name)
        
        # Small delay between conversions
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print(f"✅ Successfully converted: {successful}/{total}")
    if failed:
        print(f"❌ Failed: {len(failed)}")
        for f in failed:
            print(f"   - {f}")

if __name__ == "__main__":
    main()