# File Organizer - Python Automation Project

A practical Python script that automatically organizes messy folders and generates reports.

## What You'll Build

A command-line tool that:
- 📂 Scans any folder (like Downloads)
- 🗂️ Categorizes files by type (images, documents, videos, etc.)
- 📦 Moves files into organized subfolders
- 📊 Generates a CSV report of all actions
- 🧪 Includes a safe "dry-run" mode for testing
- ⚡ Handles errors gracefully

## What You'll Learn

✅ File system operations (os, pathlib, shutil)
✅ Working with dictionaries and lists
✅ Functions and code organization
✅ Command-line arguments (argparse)
✅ CSV file handling
✅ Error handling and logging
✅ Real-world Python scripting

## Project Structure

```
file-organizer/
├── README.md              (this file)
├── organizer.py           (main script - you'll build this)
├── config.py              (file type categories)
├── test_folder/           (practice folder with sample files)
│   ├── sample1.pdf
│   ├── photo.jpg
│   ├── video.mp4
│   └── ... (messy files)
└── reports/               (generated reports go here)
```

## Quick Start

```bash
# 1. Create project folder
mkdir file-organizer
cd file-organizer

# 2. Start with Exercise 1
# Follow the exercises in order - each builds on the previous
```

## Exercises Overview

**Exercise 1:** Scan & List Files (20 min)
- Use `os` module to list files in a folder
- Print file names and extensions

**Exercise 2:** Categorize Files (25 min)
- Create a dictionary of file types
- Match files to categories

**Exercise 3:** Create Folders (20 min)
- Create category folders if they don't exist
- Handle errors

**Exercise 4:** Move Files (Dry Run) (30 min)
- Implement dry-run mode
- Show what WOULD happen without actually moving files

**Exercise 5:** Move Files (Real) (25 min)
- Actually move the files
- Handle duplicates and errors

**Exercise 6:** Generate CSV Report (30 min)
- Create a CSV with: filename, original path, new path, category, timestamp
- Use the `csv` module

**Exercise 7:** Add Command-Line Arguments (30 min)
- Use `argparse` for CLI options
- Add flags: --dry-run, --folder, --report

**Exercise 8:** Error Handling & Logging (25 min)
- Add try/except blocks
- Log errors to a file

**Exercise 9:** Final Polish (20 min)
- Add progress indicators
- Clean up code
- Add helpful messages

**Exercise 10:** Test & Use It! (30 min)
- Organize your actual Downloads folder
- Generate reports
- Celebrate! 🎉

## Total Time: ~4 hours

## Usage (Final Script)

```bash
# Dry run (safe - shows what would happen)
python organizer.py --folder ~/Downloads --dry-run

# Actually organize files
python organizer.py --folder ~/Downloads

# With custom report location
python organizer.py --folder ~/Downloads --report ./my-report.csv

# Get help
python organizer.py --help
```

## Example Output

```
🗂️  File Organizer v1.0
📁 Scanning: /Users/you/Downloads
Found 47 files to organize

📊 Categories:
   Images: 12 files
   Documents: 23 files
   Videos: 5 files
   Audio: 3 files
   Other: 4 files

✅ Moved 47 files
📄 Report saved: report_2024-02-09.csv

Done! Your folder is organized! 🎉
```

## Git Commands (After Each Exercise)

```bash
git add .
git commit -m "Complete Exercise X: [description]"
git push origin main
```

## Ready?

Start with **Exercise 1** in the exercises folder!
