# Exercise 1: Scan and List Files

**Time:** 20 minutes  
**Goal:** Learn to navigate and read files from a folder using Python

## What You'll Learn
- Using the `os` module
- Listing files in a directory
- Getting file extensions
- Basic string manipulation

## Your Task

Create a script that:
1. Takes a folder path
2. Lists all files (not folders)
3. Shows each file's name and extension

## Example Output

```
Scanning folder: ./test_folder
Found 5 files:

1. document.pdf (.pdf)
2. photo.jpg (.jpg)
3. video.mp4 (.mp4)
4. notes.txt (.txt)
5. report.docx (.docx)
```

## Starter Code

```python
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
    
    # TODO: Use os.listdir() to get all items in folder
    # TODO: Filter out directories, keep only files
    # Hint: use os.path.isfile()
    
    return files

def get_extension(filename):
    """
    Get file extension from filename.
    
    Args:
        filename: Name of file
        
    Returns:
        Extension (including the dot)
    """
    # TODO: Split filename by '.' and get the last part
    # Hint: use .split('.')
    pass

# Test your code
if __name__ == "__main__":
    folder = "./test_folder"
    
    print(f"Scanning folder: {folder}")
    files = scan_folder(folder)
    print(f"Found {len(files)} files:\n")
    
    for i, filename in enumerate(files, 1):
        ext = get_extension(filename)
        print(f"{i}. {filename} ({ext})")
```

## Hints

### Getting files from a folder:
```python
import os

# List everything in folder
items = os.listdir(folder_path)

# Check if item is a file
for item in items:
    full_path = os.path.join(folder_path, item)
    if os.path.isfile(full_path):
        print(f"{item} is a file")
```

### Getting file extension:
```python
filename = "document.pdf"
parts = filename.split('.')
extension = '.' + parts[-1]  # Gets '.pdf'
```

Or use the easy way:
```python
import os
filename = "document.pdf"
name, ext = os.path.splitext(filename)  # ext = '.pdf'
```

## Testing Your Code

Run your script:
```bash
python exercise_1.py
```

## Success Checklist

- [ ] Script lists all files in test_folder
- [ ] Shows correct file extensions
- [ ] Doesn't include folders in the list
- [ ] Handles empty folders gracefully

## Common Issues

**Problem:** "FileNotFoundError"  
**Solution:** Make sure test_folder exists or use an absolute path

**Problem:** Script includes folders  
**Solution:** Use `os.path.isfile()` to filter

## Next Steps

Once working, commit your code:
```bash
git add exercise_1.py
git commit -m "Complete Exercise 1: Scan and list files"
git push
```

Then move to **Exercise 2: Categorize Files**!
