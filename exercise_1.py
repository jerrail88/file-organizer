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
    
    # Get all items in folder
    items = os.listdir(folder_path)
    
    # Filter out directories, keep only files
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
    # Use os.path.splitext
    name, ext = os.path.splitext(filename)
    return ext.lower()

# Test your code
if __name__ == "__main__":
    folder = "./test_folder"
    
    print(f"Scanning folder: {folder}")
    files = scan_folder(folder)
    print(f"Found {len(files)} files:\n")
    
    for i, filename in enumerate(files, 1):
        ext = get_extension(filename)
        print(f"{i}. {filename} ({ext})")
