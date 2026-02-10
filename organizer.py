"""
File Organizer - Automated file organization tool
Organizes files in a folder by type and generates a report
"""

import os
import shutil
import csv
import argparse
import logging
from datetime import datetime
from pathlib import Path
from config import FILE_CATEGORIES, get_category

# Setup logging
logging.basicConfig(
    filename='organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scan_folder(folder_path):
    """
    Scan folder and return list of files (not directories).
    
    Args:
        folder_path: Path to folder to scan
        
    Returns:
        List of file paths
    """
    files = []
    
    try:
        for item in os.listdir(folder_path):
            full_path = os.path.join(folder_path, item)
            if os.path.isfile(full_path):
                files.append(full_path)
        
        logging.info(f"Scanned folder: {folder_path}, found {len(files)} files")
        return files
        
    except Exception as e:
        logging.error(f"Error scanning folder {folder_path}: {e}")
        return []

def categorize_files(files):
    """
    Organize files into categories based on extension.
    
    Args:
        files: List of file paths
        
    Returns:
        Dictionary with categories as keys and file lists as values
    """
    categorized = {}
    
    for filepath in files:
        filename = os.path.basename(filepath)
        _, ext = os.path.splitext(filename)
        category = get_category(ext)
        
        if category not in categorized:
            categorized[category] = []
        
        categorized[category].append(filepath)
    
    return categorized

def create_category_folders(base_path, categories):
    """
    Create folders for each category.
    
    Args:
        base_path: Base directory where folders will be created
        categories: List of category names
    """
    for category in categories:
        folder_path = os.path.join(base_path, category)
        try:
            os.makedirs(folder_path, exist_ok=True)
            logging.info(f"Created folder: {folder_path}")
        except Exception as e:
            logging.error(f"Error creating folder {folder_path}: {e}")

def get_unique_filename(destination):
    """
    Generate unique filename if file already exists.
    
    Args:
        destination: Target file path
        
    Returns:
        Unique file path
    """
    if not os.path.exists(destination):
        return destination
    
    base, ext = os.path.splitext(destination)
    counter = 1
    
    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1
    
    return f"{base}_{counter}{ext}"

def move_files(categorized, base_path, dry_run=False):
    """
    Move files to their category folders.
    
    Args:
        categorized: Dictionary of categorized files
        base_path: Base directory
        dry_run: If True, don't actually move files
        
    Returns:
        List of dictionaries with move operation details
    """
    operations = []
    
    for category, files in categorized.items():
        category_folder = os.path.join(base_path, category)
        
        for filepath in files:
            filename = os.path.basename(filepath)
            destination = os.path.join(category_folder, filename)
            destination = get_unique_filename(destination)
            
            operation = {
                'timestamp': datetime.now().isoformat(),
                'filename': filename,
                'original_path': filepath,
                'new_path': destination,
                'category': category,
                'size_bytes': os.path.getsize(filepath) if os.path.exists(filepath) else 0,
                'status': 'Pending'
            }
            
            if dry_run:
                operation['status'] = 'Dry Run'
                logging.info(f"[DRY RUN] Would move: {filepath} → {destination}")
            else:
                try:
                    shutil.move(filepath, destination)
                    operation['status'] = 'Success'
                    logging.info(f"Moved: {filepath} → {destination}")
                except Exception as e:
                    operation['status'] = f'Error: {str(e)}'
                    logging.error(f"Failed to move {filepath}: {e}")
            
            operations.append(operation)
    
    return operations

def generate_report(operations, report_path):
    """
    Generate CSV report of file operations.
    
    Args:
        operations: List of operation dictionaries
        report_path: Path where report will be saved
    """
    try:
        with open(report_path, 'w', newline='', encoding='utf-8') as f:
            if operations:
                fieldnames = operations[0].keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(operations)
        
        logging.info(f"Report saved: {report_path}")
        print(f"\n📄 Report saved: {report_path}")
        
    except Exception as e:
        logging.error(f"Error generating report: {e}")
        print(f"✗ Error saving report: {e}")

def display_summary(categorized, operations, dry_run=False):
    """Display summary of operations."""
    print("\n" + "="*50)
    print("📊 SUMMARY")
    print("="*50)
    
    total_files = sum(len(files) for files in categorized.values())
    print(f"\nTotal files: {total_files}")
    
    print("\nBy category:")
    for category, files in sorted(categorized.items()):
        print(f"  {category}: {len(files)} files")
    
    if not dry_run:
        successful = sum(1 for op in operations if op['status'] == 'Success')
        failed = sum(1 for op in operations if op['status'].startswith('Error'))
        
        print(f"\n✓ Successfully moved: {successful}")
        if failed > 0:
            print(f"✗ Failed: {failed}")
    
    print("="*50 + "\n")

def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='🗂️  File Organizer - Automatically organize files by type',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python organizer.py --folder ~/Downloads --dry-run
  python organizer.py --folder ~/Desktop --report my-report.csv
  python organizer.py --help
        """
    )
    
    parser.add_argument(
        '--folder',
        default='./test_folder',
        help='Folder to organize (default: ./test_folder)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would happen without moving files'
    )
    
    parser.add_argument(
        '--report',
        default='./reports/report.csv',
        help='Output report path (default: ./reports/report.csv)'
    )
    
    args = parser.parse_args()
    
    # Convert to absolute path
    folder_path = os.path.abspath(args.folder)
    
    # Print header
    print("\n" + "="*50)
    print("🗂️  FILE ORGANIZER v1.0")
    print("="*50)
    
    if args.dry_run:
        print("\n🧪 DRY RUN MODE (no files will be moved)\n")
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"\n✗ Error: Folder '{folder_path}' does not exist!")
        return
    
    # Scan folder
    print(f"\n📁 Scanning: {folder_path}")
    files = scan_folder(folder_path)
    
    if not files:
        print("\n📭 No files found in this folder!")
        return
    
    print(f"Found {len(files)} files")
    
    # Categorize files
    categorized = categorize_files(files)
    
    # Create category folders (skip in dry-run)
    if not args.dry_run:
        categories = list(categorized.keys())
        create_category_folders(folder_path, categories)
    
    # Move files
    print(f"\n{'📋 Preview' if args.dry_run else '📦 Organizing files'}...")
    operations = move_files(categorized, folder_path, dry_run=args.dry_run)
    
    # Display summary
    display_summary(categorized, operations, args.dry_run)
    
    # Generate report
    if operations:
        # Ensure reports directory exists
        report_dir = os.path.dirname(args.report)
        if report_dir and not os.path.exists(report_dir):
            os.makedirs(report_dir, exist_ok=True)
        
        generate_report(operations, args.report)
    
    if args.dry_run:
        print("💡 Run without --dry-run to actually organize files\n")
    else:
        print("✅ Done! Your files are organized! 🎉\n")

if __name__ == "__main__":
    main()
