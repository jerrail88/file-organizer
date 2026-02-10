# File Organizer - All Exercises

## Exercise 3: Create Organized Folders
**Time:** 20 min | **File:** `exercise_3.py`

Create the category folders before moving files.

**Key Concepts:**
- `os.makedirs()`
- Error handling with try/except
- Creating nested directories

**Task:**
```python
def create_category_folders(base_path, categories):
    """Create a folder for each category"""
    for category in categories:
        folder_path = os.path.join(base_path, category)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"✓ Created: {category}/")
        except Exception as e:
            print(f"✗ Error creating {category}: {e}")
```

---

## Exercise 4: Dry Run Mode
**Time:** 30 min | **File:** `exercise_4.py`

Implement a safe mode that shows what WOULD happen without actually moving files.

**Key Concepts:**
- Conditional logic
- Function parameters with defaults
- Simulating actions

**Task:**
- Add `dry_run=True` parameter to functions
- Print what would happen instead of doing it
- Use different output symbols (would move → vs moved ✓)

**Example Output:**
```
🧪 DRY RUN MODE (no files will be moved)

Would move:
  photo.jpg → Images/photo.jpg
  document.pdf → Documents/document.pdf
  
Summary: 10 files would be organized
```

---

## Exercise 5: Move Files
**Time:** 25 min | **File:** `exercise_5.py`

Actually move the files to organized folders.

**Key Concepts:**
- `shutil.move()`
- Handling duplicate filenames
- Path manipulation

**Task:**
```python
import shutil

def move_file(source, destination, dry_run=False):
    """Move a file from source to destination"""
    if dry_run:
        print(f"  Would move: {source} → {destination}")
        return
    
    try:
        shutil.move(source, destination)
        print(f"  ✓ Moved: {os.path.basename(source)}")
    except Exception as e:
        print(f"  ✗ Error: {e}")
```

**Handle Duplicates:**
If `photo.jpg` already exists, rename to `photo_1.jpg`, `photo_2.jpg`, etc.

---

## Exercise 6: Generate CSV Report
**Time:** 30 min | **File:** `exercise_6.py`

Create a detailed CSV report of all file movements.

**Key Concepts:**
- `csv` module
- Writing structured data
- Timestamps with `datetime`

**Task:**
Create CSV with columns:
- Timestamp
- Filename
- Original Path
- New Path
- Category
- File Size
- Status (Success/Error)

**Example CSV:**
```csv
timestamp,filename,original_path,new_path,category,size_bytes,status
2024-02-09 14:30:22,photo.jpg,/Downloads/photo.jpg,/Downloads/Images/photo.jpg,Images,245678,Success
2024-02-09 14:30:23,doc.pdf,/Downloads/doc.pdf,/Downloads/Documents/doc.pdf,Documents,98234,Success
```

---

## Exercise 7: Command-Line Arguments
**Time:** 30 min | **File:** `exercise_7.py`

Add proper CLI using argparse.

**Key Concepts:**
- `argparse` module
- Optional and required arguments
- Help text

**Task:**
```python
import argparse

parser = argparse.ArgumentParser(
    description='Organize files into categorized folders'
)

parser.add_argument(
    '--folder',
    default='.',
    help='Folder to organize (default: current directory)'
)

parser.add_argument(
    '--dry-run',
    action='store_true',
    help='Show what would happen without moving files'
)

parser.add_argument(
    '--report',
    default='report.csv',
    help='Output report filename'
)

args = parser.parse_args()
```

**Usage:**
```bash
python organizer.py --folder ~/Downloads --dry-run
python organizer.py --folder ~/Desktop --report my-report.csv
```

---

## Exercise 8: Error Handling & Logging
**Time:** 25 min | **File:** `exercise_8.py`

Add comprehensive error handling and logging.

**Key Concepts:**
- try/except/finally
- logging module
- Error types

**Task:**
```python
import logging

# Setup logging
logging.basicConfig(
    filename='organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log different events
logging.info("Started organizing folder: /Downloads")
logging.warning("Duplicate file found: photo.jpg")
logging.error("Failed to move file: permission denied")
```

**Handle These Errors:**
- Folder doesn't exist
- No permission to read/write
- Disk space issues
- Invalid file names

---

## Exercise 9: Final Polish
**Time:** 20 min | **File:** `exercise_9.py`

Add user-friendly features.

**Features to Add:**
1. **Progress Bar** (using tqdm or simple counter)
2. **Confirmation Prompt** (before moving files)
3. **Summary Statistics**
4. **Color Output** (using colorama)
5. **Undo Option** (save original locations)

**Example:**
```python
from tqdm import tqdm

for file in tqdm(files, desc="Organizing files"):
    # Move file
    pass
```

---

## Exercise 10: Final Integration
**Time:** 30 min | **File:** `organizer.py`

Combine everything into one polished script.

**Checklist:**
- [ ] All functions work together
- [ ] Clean code with docstrings
- [ ] Error handling everywhere
- [ ] CLI arguments work
- [ ] Generates report
- [ ] Dry-run mode works
- [ ] Good user feedback
- [ ] Logging enabled
- [ ] README updated with usage

**Test It:**
1. Test on test_folder with --dry-run
2. Actually organize test_folder
3. Check the CSV report
4. Try on real Downloads folder
5. Check logs

**Celebrate!** 🎉 You built a real automation tool!

---

## Git Workflow

After each exercise:
```bash
git add .
git commit -m "Complete Exercise X: [what you built]"
git push origin main
```

## Next Level

Want to go further?
- Add GUI with tkinter
- Schedule automatic organization (cron/Task Scheduler)
- Add file preview
- Email reports
- Watch folder for new files
- Undo functionality with backup
- Custom category rules
- Integration with cloud storage
