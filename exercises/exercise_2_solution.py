"""
Exercise 2: Categorize Files
Solution
"""

import os

# File type categories
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.odt', '.rtf'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.json', '.xml'],
}

def get_category(extension):
    """
    Determine which category a file belongs to based on extension.
    
    Args:
        extension: File extension (e.g., '.pdf')
        
    Returns:
        Category name (e.g., 'Documents') or 'Other'
    """
    extension = extension.lower()  # Make case-insensitive
    
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    
    return 'Other'

def categorize_files(files):
    """
    Organize files into categories.
    
    Args:
        files: List of filenames
        
    Returns:
        Dictionary where keys are categories and values are lists of files
    """
    categorized = {}
    
    for filename in files:
        # Get extension
        _, ext = os.path.splitext(filename)
        
        # Get category
        category = get_category(ext)
        
        # Add to dictionary (create list if category doesn't exist)
        if category not in categorized:
            categorized[category] = []
        
        categorized[category].append(filename)
    
    return categorized

def scan_folder(folder_path):
    """Scan folder and return list of files."""
    files = []
    
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist!")
        return files
    
    items = os.listdir(folder_path)
    
    for item in items:
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            files.append(item)
    
    return files

# Test the code
if __name__ == "__main__":
    folder = "./test_folder"
    
    print(f"📁 Scanning: {folder}")
    files = scan_folder(folder)
    print(f"Found {len(files)} files\n")
    
    if not files:
        print("No files found! Add some test files to test_folder/")
        print("\nExample:")
        print("  cd test_folder")
        print("  touch photo.jpg video.mp4 report.pdf notes.txt music.mp3")
    else:
        # Categorize the files
        categorized = categorize_files(files)
        
        # Display results
        print("📊 File Categories:")
        print("━" * 40)
        
        # Sort categories to show them in consistent order
        for category in sorted(categorized.keys()):
            file_list = categorized[category]
            count = len(file_list)
            
            print(f"\n{category} ({count} file{'s' if count != 1 else ''}):")
            for filename in sorted(file_list):
                print(f"  - {filename}")
