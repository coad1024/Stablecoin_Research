#!/usr/bin/env python3
"""
PDF to Markdown Converter using Marker
High-quality conversion of research papers with Marker's advanced features.
"""

import os
import sys
from pathlib import Path
import logging
from typing import List, Tuple, Optional
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def find_pdf_files(papers_dir: Path) -> List[Path]:
    """Find all PDF files in the papers directory."""
    pdf_files = list(papers_dir.glob("*.pdf"))
    return sorted(pdf_files)

def convert_pdf_with_marker(
    pdf_path: Path, 
    output_dir: Path, 
    use_llm: bool = False,
    force_ocr: bool = False,
    output_format: str = "markdown"
) -> Tuple[bool, str]:
    """
    Convert a single PDF to markdown using Marker.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the markdown file
        use_llm: Whether to use LLM for enhanced quality
        force_ocr: Whether to force OCR (improves equation handling)
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        from marker.converters.pdf import PdfConverter
        from marker.models import create_model_dict
        from marker.output import text_from_rendered
        
        logger.info(f"Converting: {pdf_path.name}")
        start_time = time.time()
        
        # Configuration
        config = {"output_format": output_format}
        if use_llm:
            config["use_llm"] = True
            logger.info("  Using LLM for enhanced quality")
        if force_ocr:
            config["force_ocr"] = True
            logger.info("  Forcing OCR for better equation handling")
        if output_format != "markdown":
            logger.info(f"  Output format: {output_format}")
        
        # Create converter
        converter = PdfConverter(
            artifact_dict=create_model_dict(),
            config=config
        )
        
        # Convert the PDF
        rendered = converter(str(pdf_path))
        
        # Extract text and metadata
        text, metadata, images = text_from_rendered(rendered)
        
        # Save output based on format
        import json
        
        # Save based on output format(s)
        saved_files = []
        if output_format in ["markdown", "both"]:
            output_filename = pdf_path.stem + ".md"
            output_path = output_dir / output_filename
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            saved_files.append(output_filename)
        
        if output_format in ["json", "both"]:
            output_filename = pdf_path.stem + ".json"
            output_path = output_dir / output_filename
            # Save the full rendered output as JSON
            with open(output_path, 'w', encoding='utf-8') as f:
                # Convert the pydantic model to dict
                if hasattr(rendered, 'model_dump'):
                    output_data = rendered.model_dump(mode='json')
                elif hasattr(rendered, 'dict'):
                    output_data = rendered.dict()
                else:
                    # Fallback to manual conversion
                    output_data = {
                        "text": text,
                        "metadata": metadata
                    }
                json.dump(output_data, f, indent=2, ensure_ascii=False, default=str)
            saved_files.append(output_filename)
        
        # Save images if any
        if images:
            images_dir = output_dir / f"{pdf_path.stem}_images"
            images_dir.mkdir(exist_ok=True)
            saved_images = 0
            for img_name, img_data in images.items():
                try:
                    img_path = images_dir / img_name
                    # Handle PIL Image objects
                    if hasattr(img_data, 'save'):
                        # It's a PIL Image object
                        img_data.save(str(img_path))
                        saved_images += 1
                    elif isinstance(img_data, bytes):
                        # It's raw bytes
                        with open(img_path, 'wb') as f:
                            f.write(img_data)
                        saved_images += 1
                except Exception as e:
                    logger.warning(f"    Could not save image {img_name}: {e}")
            if saved_images > 0:
                logger.info(f"  ✓ Saved {saved_images} images to {images_dir.name}/")
        
        elapsed = time.time() - start_time
        files_msg = " & ".join(saved_files) if saved_files else output_path.name
        logger.info(f"  ✓ Converted in {elapsed:.1f}s → {files_msg}")
        
        return True, f"Successfully converted {pdf_path.name}"
        
    except ImportError as e:
        error_msg = f"Marker not installed properly: {str(e)}"
        logger.error(f"  ✗ {error_msg}")
        logger.info("Install with: poetry add marker-pdf")
        return False, error_msg
    except Exception as e:
        error_msg = f"Failed to convert {pdf_path.name}: {str(e)}"
        logger.error(f"  ✗ {error_msg}")
        return False, error_msg

def main():
    """Main function to convert all PDFs using Marker."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Convert PDFs to Markdown using Marker")
    parser.add_argument(
        "--input-dir", 
        type=str, 
        default="papers",
        help="Input directory containing PDFs (default: papers)"
    )
    parser.add_argument(
        "--output-dir", 
        type=str, 
        default="papers_markdown_marker",
        help="Output directory for markdown files (default: papers_markdown_marker)"
    )
    parser.add_argument(
        "--use-llm", 
        action="store_true",
        help="Use LLM for enhanced quality (requires API key setup)"
    )
    parser.add_argument(
        "--force-ocr", 
        action="store_true",
        help="Force OCR on all pages (better for equations)"
    )
    parser.add_argument(
        "--single", 
        type=str,
        help="Convert only a single PDF file (specify filename)"
    )
    parser.add_argument(
        "--max-files",
        type=int,
        help="Maximum number of files to convert"
    )
    parser.add_argument(
        "--output-format",
        type=str,
        choices=["markdown", "json", "html", "chunks", "both"],
        default="markdown",
        help="Output format - use 'both' for markdown AND json (default: markdown)"
    )
    
    args = parser.parse_args()
    
    try:
        # Setup directories
        project_root = Path.cwd()
        papers_dir = project_root / args.input_dir
        output_dir = project_root / args.output_dir
        
        if not papers_dir.exists():
            logger.error(f"Input directory not found: {papers_dir}")
            sys.exit(1)
        
        output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Output directory: {output_dir}")
        
        # Find PDFs to convert
        if args.single:
            pdf_path = papers_dir / args.single
            if not pdf_path.exists():
                logger.error(f"PDF not found: {pdf_path}")
                sys.exit(1)
            pdf_files = [pdf_path]
        else:
            pdf_files = find_pdf_files(papers_dir)
            if args.max_files:
                pdf_files = pdf_files[:args.max_files]
        
        if not pdf_files:
            logger.warning("No PDF files found to convert")
            sys.exit(0)
        
        # Test import first
        try:
            import marker
            logger.info(f"✓ Marker is installed")
        except ImportError:
            logger.error("Marker is not installed!")
            logger.info("Install with: poetry add marker-pdf")
            sys.exit(1)
        
        logger.info(f"Found {len(pdf_files)} PDF files to convert")
        if args.use_llm:
            logger.info("🤖 LLM enhancement enabled")
        if args.force_ocr:
            logger.info("🔍 Force OCR enabled")
        logger.info("-" * 50)
        
        # Convert PDFs
        successful = 0
        failed = 0
        failed_files = []
        total_start = time.time()
        
        for i, pdf_path in enumerate(pdf_files, 1):
            logger.info(f"\n[{i}/{len(pdf_files)}] Processing {pdf_path.name}")
            success, message = convert_pdf_with_marker(
                pdf_path, 
                output_dir,
                use_llm=args.use_llm,
                force_ocr=args.force_ocr,
                output_format=args.output_format
            )
            if success:
                successful += 1
            else:
                failed += 1
                failed_files.append(pdf_path.name)
        
        # Summary
        total_time = time.time() - total_start
        logger.info("\n" + "=" * 50)
        logger.info("📊 Conversion Summary:")
        logger.info(f"  ✅ Successful: {successful}/{len(pdf_files)}")
        
        if failed > 0:
            logger.warning(f"  ❌ Failed: {failed}")
            for fname in failed_files:
                logger.warning(f"     - {fname}")
        
        logger.info(f"  ⏱️  Total time: {total_time:.1f}s")
        logger.info(f"  📁 Output directory: {output_dir}")
        
        if successful > 0:
            logger.info("\n✨ Conversion complete! Markdown files are ready.")
        
    except KeyboardInterrupt:
        logger.info("\n⚠️ Conversion interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()