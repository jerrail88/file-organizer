"""
Exercise 1: Scan and List Files
Solution
"""

import os

def scan_folder(folder_path):
    """
    Scan a folder and return list of files.
    
    Args:
        folder_path: Path to folder to scan
        
    Returns:
        List of filenames
    """
    files = []
    
    # Get all items in the folder
    items = os.listdir(folder_path)
    
    # Filter to keep only files (not directories)
    for item in items:
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            files.append(item)
    
    return files

def get_extension(filename):
    """
    Get file extension from filename.
    
    Args:
        filename: Name of file
        
    Returns:
        Extension (including the dot)
    """
    # Use os.path.splitext for easy extension extraction
    name, ext = os.path.splitext(filename)
    return ext.lower()  # Return lowercase for consistency

# Test the code
if __name__ == "__main__":
    folder = "./test_folder"
    
    # Check if folder exists
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist!")
        print("Creating test_folder...")
        os.makedirs(folder, exist_ok=True)
        print("Please add some test files to test_folder/")
    else:
        print(f"📁 Scanning folder: {folder}")
        files = scan_folder(folder)
        
        if not files:
            print("No files found! Add some files to test_folder/")
        else:
            print(f"Found {len(files)} files:\n")
            
            for i, filename in enumerate(files, 1):
                ext = get_extension(filename)
                print(f"{i}. {filename} ({ext})")
