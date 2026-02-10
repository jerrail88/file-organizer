# Quick Start Guide

## Setup (5 minutes)

### 1. Extract the Project
```bash
# Extract the downloaded zip file
unzip file-organizer.zip
cd file-organizer
```

### 2. Test the Script
```bash
# Run in dry-run mode first (safe - won't move anything)
python organizer.py --dry-run
```

You should see:
```
🗂️  FILE ORGANIZER v1.0
🧪 DRY RUN MODE (no files will be moved)

📁 Scanning: /path/to/file-organizer/test_folder
Found 10 files

📋 Preview...

📊 SUMMARY
Total files: 10

By category:
  Images: 2 files
  Documents: 3 files
  Videos: 1 file
  Audio: 1 file
  Archives: 1 file
  Code: 1 file
  Other: 1 file

📄 Report saved: ./reports/report.csv
```

### 3. Actually Organize Files
```bash
# Now organize for real
python organizer.py
```

### 4. Check the Results
```bash
# Look at the organized folders
ls test_folder/

# Check the report
cat reports/report.csv
```

## Use on Your Real Folders

### Organize Downloads (SAFELY!)
```bash
# Always test with dry-run first!
python organizer.py --folder ~/Downloads --dry-run

# If it looks good, run for real
python organizer.py --folder ~/Downloads
```

### Organize Desktop
```bash
python organizer.py --folder ~/Desktop --dry-run
python organizer.py --folder ~/Desktop
```

### Custom Report Name
```bash
python organizer.py --folder ~/Downloads --report downloads-cleanup-feb-9.csv
```

## Git Workflow

### First Time Setup
```bash
# Initialize Git
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: File organizer project"

# Create GitHub repo, then:
git remote add origin https://github.com/YOUR_USERNAME/file-organizer.git
git branch -M main
git push -u origin main
```

### After Each Exercise
```bash
git add .
git commit -m "Complete Exercise X: [description]"
git push origin main
```

## What Each File Does

```
file-organizer/
├── README.md              # Main documentation
├── organizer.py           # Main script (complete solution)
├── config.py              # File type definitions
├── .gitignore            # Git ignore rules
├── exercises/            # Learning exercises
│   ├── exercise_1.md     # Scan & list files
│   ├── exercise_2.md     # Categorize files
│   ├── ALL_EXERCISES.md  # All 10 exercises
│   └── *_solution.py     # Reference solutions
├── test_folder/          # Practice folder with sample files
└── reports/              # Generated CSV reports go here
```

## Learning Path

### For Beginners
1. Start with `exercises/exercise_1.md`
2. Work through each exercise in order
3. Compare with solution files when stuck
4. Build up to the complete organizer.py

### For Quick Start
1. Just use `organizer.py` - it's the complete working script
2. Read the code to understand how it works
3. Modify it for your needs

## Common Use Cases

### Organize Downloads Automatically
Add to your shell profile:
```bash
alias cleanup-downloads='python ~/file-organizer/organizer.py --folder ~/Downloads'
```

### Schedule Regular Organization
Add to crontab (runs every day at 6 PM):
```bash
0 18 * * * python ~/file-organizer/organizer.py --folder ~/Downloads
```

### Before Important File Moves
```bash
# Always dry-run first!
python organizer.py --folder /important/folder --dry-run

# Review what would happen, then:
python organizer.py --folder /important/folder
```

## Tips

✅ **Always use --dry-run first** on important folders
✅ **Check the CSV report** to see exactly what happened
✅ **Start with test_folder** to get comfortable
✅ **Customize FILE_CATEGORIES** in config.py for your needs
✅ **Check organizer.log** if something goes wrong

## Get Help

```bash
python organizer.py --help
```

## Next Steps

1. ✅ Test on test_folder
2. ✅ Try on Downloads with --dry-run
3. ✅ Organize for real
4. ✅ Check the CSV report
5. ✅ Customize categories in config.py
6. ✅ Add your own file types
7. ✅ Share with friends!

Happy organizing! 🗂️
