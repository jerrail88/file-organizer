# Exercise 2: Categorize Files

**Time:** 25 minutes  
**Goal:** Group files into categories based on their extensions

## What You'll Learn
- Working with dictionaries
- Organizing data
- Categorizing based on conditions
- Using defaultdict (optional)

## Your Task

Create a system that categorizes files into groups:
- **Images:** .jpg, .jpeg, .png, .gif, .bmp, .svg
- **Documents:** .pdf, .doc, .docx, .txt, .xlsx, .pptx
- **Videos:** .mp4, .avi, .mkv, .mov, .wmv
- **Audio:** .mp3, .wav, .flac, .aac
- **Archives:** .zip, .rar, .tar, .gz, .7z
- **Code:** .py, .js, .html, .css, .java, .cpp
- **Other:** Everything else

## Example Output

```
📁 Scanning: ./test_folder
Found 8 files

📊 File Categories:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Images (3 files):
  - photo.jpg
  - screenshot.png
  - logo.gif

Documents (3 files):
  - report.pdf
  - notes.txt
  - presentation.pptx

Videos (1 file):
  - movie.mp4

Other (1 file):
  - data.dat
```

## Starter Code

```python
import os

# File type categories
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.odt'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h'],
}

def get_category(extension):
    """
    Determine which category a file belongs to based on extension.
    
    Args:
        extension: File extension (e.g., '.pdf')
        
    Returns:
        Category name (e.g., 'Documents') or 'Other'
    """
    # TODO: Loop through FILE_CATEGORIES
    # TODO: Check if extension is in the list of extensions for each category
    # TODO: Return the category name if found
    # TODO: Return 'Other' if not found in any category
    pass

def categorize_files(files):
    """
    Organize files into categories.
    
    Args:
        files: List of filenames
        
    Returns:
        Dictionary where keys are categories and values are lists of files
    """
    categorized = {}
    
    # TODO: For each file:
    # 1. Get its extension
    # 2. Get its category
    # 3. Add it to the appropriate category list in the dictionary
    
    return categorized

def scan_folder(folder_path):
    """Scan folder and return list of files."""
    files = []
    items = os.listdir(folder_path)
    
    for item in items:
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            files.append(item)
    
    return files

# Test your code
if __name__ == "__main__":
    folder = "./test_folder"
    
    print(f"📁 Scanning: {folder}")
    files = scan_folder(folder)
    print(f"Found {len(files)} files\n")
    
    # Categorize the files
    categorized = categorize_files(files)
    
    # Display results
    print("📊 File Categories:")
    print("━" * 30)
    
    for category, file_list in categorized.items():
        if file_list:  # Only show categories that have files
            count = len(file_list)
            print(f"\n{category} ({count} file{'s' if count != 1 else ''}):")
            for filename in file_list:
                print(f"  - {filename}")
```

## Hints

### Checking if extension is in a category:
```python
extension = '.pdf'
category_extensions = ['.pdf', '.doc', '.docx']

if extension in category_extensions:
    print("It's a document!")
```

### Building a dictionary of lists:
```python
result = {}

# Add to a category (create list if it doesn't exist)
category = 'Documents'
filename = 'report.pdf'

if category not in result:
    result[category] = []

result[category].append(filename)
```

### Alternative (cleaner) using get():
```python
result.setdefault(category, []).append(filename)
```

## Testing Your Code

1. Create test files in test_folder:
```bash
cd test_folder
touch photo.jpg video.mp4 report.pdf notes.txt music.mp3
```

2. Run your script:
```bash
python exercise_2.py
```

## Success Checklist

- [ ] Correctly categorizes all common file types
- [ ] Shows count for each category
- [ ] Lists files under their category
- [ ] Handles 'Other' category for unknown types
- [ ] Works with uppercase and lowercase extensions

## Challenge

Add a function to show statistics:
- Total files
- Largest category
- Empty categories

## Next Steps

```bash
git add exercise_2.py
git commit -m "Complete Exercise 2: Categorize files by type"
git push
```

Move to **Exercise 3: Create Organized Folders**!
