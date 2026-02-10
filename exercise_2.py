import os

FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
}

def get_category(extension):
    extension = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return 'Other'

def categorize_files(files):
    categorized = {}
    for filename in files:
        _, ext = os.path.splitext(filename)
        category = get_category(ext)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(filename)
    return categorized

def scan_folder(folder_path):
    files = []
    items = os.listdir(folder_path)
    for item in items:
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            files.append(item)
    return files

if __name__ == "__main__":
    folder = "./test_folder"
    print(f"Scanning: {folder}")
    files = scan_folder(folder)
    print(f"Found {len(files)} files\n")
    categorized = categorize_files(files)
    print("File Categories:")
    print("-" * 40)
    for category in sorted(categorized.keys()):
        file_list = categorized[category]
        count = len(file_list)
        print(f"\n{category} ({count} file{'s' if count != 1 else ''}):")
        for filename in sorted(file_list):
            print(f"  - {filename}")
