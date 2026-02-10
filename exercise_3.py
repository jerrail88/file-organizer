import os
import shutil

FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
}

def get_category(extension):
    """Get category for a file extension."""
    extension = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return 'Other'

def scan_folder(folder_path):
    """Scan folder and return list of files."""
    files = []
    items = os.listdir(folder_path)
    for item in items:
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            files.append(item)
    return files

def categorize_files(files):
    """Organize files into categories."""
    categorized = {}
    for filename in files:
        _, ext = os.path.splitext(filename)
        category = get_category(ext)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(filename)
    return categorized

def create_category_folders(base_path, categories, dry_run=False):
    """
    Create folders for each category.
    
    Args:
        base_path: Base directory where folders will be created
        categories: List of category names
        dry_run: If True, only show what would be created
    """
    print("\n📁 Creating category folders...")
    
    for category in categories:
        folder_path = os.path.join(base_path, category)
        
        if dry_run:
            if not os.path.exists(folder_path):
                print(f"  Would create: {category}/")
            else:
                print(f"  Already exists: {category}/")
        else:
            try:
                os.makedirs(folder_path, exist_ok=True)
                print(f"  ✓ Created: {category}/")
            except Exception as e:
                print(f"  ✗ Error creating {category}/: {e}")

def move_files(categorized, base_path, dry_run=False):
    """
    Move files to their category folders.
    
    Args:
        categorized: Dictionary of categorized files
        base_path: Base directory
        dry_run: If True, only show what would be moved
    """
    moved_count = 0
    
    print(f"\n{'🧪 DRY RUN - Simulating file moves...' if dry_run else '📦 Moving files...'}")
    
    for category, files in categorized.items():
        category_folder = os.path.join(base_path, category)
        
        for filename in files:
            source = os.path.join(base_path, filename)
            destination = os.path.join(category_folder, filename)
            
            if dry_run:
                print(f"  Would move: {filename} → {category}/{filename}")
                moved_count += 1
            else:
                try:
                    shutil.move(source, destination)
                    print(f"  ✓ Moved: {filename} → {category}/")
                    moved_count += 1
                except Exception as e:
                    print(f"  ✗ Error moving {filename}: {e}")
    
    return moved_count

def main():
    """Main function."""
    folder = "./test_folder"
    dry_run = True  # Set to False to actually move files
    
    print("=" * 50)
    print("🗂️  FILE ORGANIZER - Exercise 3")
    print("=" * 50)
    
    if dry_run:
        print("\n🧪 DRY RUN MODE (no files will be moved)")
    
    # Scan folder
    print(f"\n📁 Scanning: {folder}")
    files = scan_folder(folder)
    print(f"Found {len(files)} files")
    
    if not files:
        print("\n📭 No files to organize!")
        return
    
    # Categorize files
    categorized = categorize_files(files)
    
    # Show what will be organized
    print("\n📊 Files to organize:")
    for category, file_list in sorted(categorized.items()):
        print(f"  {category}: {len(file_list)} files")
    
    # Create folders
    categories = list(categorized.keys())
    create_category_folders(folder, categories, dry_run)
    
    # Move files
    moved = move_files(categorized, folder, dry_run)
    
    # Summary
    print("\n" + "=" * 50)
    if dry_run:
        print(f"✅ Dry run complete! {moved} files would be organized.")
        print("\n💡 Set dry_run=False in the code to actually move files")
    else:
        print(f"✅ Done! Organized {moved} files.")
    print("=" * 50)

if __name__ == "__main__":
    main()
