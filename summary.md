# Project Summary: Duplicate Finder

## Overview

`find_duplicates.py` is a command-line Python program that checks a text file for duplicate lines. It reports how many items are repeated, how often, and saves a cleaned, de-duplicated list to `unique.txt`.

## What It Does

1. Asks for a file name and reads it line by line.
2. Handles a missing file or an empty file with a clear message.
3. Offers two comparison modes:
   - **Exact match**
   - **Ignore case and extra spaces**
4. Counts total and unique items.
5. Lists each duplicated entry with its repeat count.
6. Writes the unique entries, in original order, to `unique.txt`.

## Key Concepts Used

- **File handling:** `open()`, `try/except FileNotFoundError`, reading and writing text files
- **Sets:** to identify unique entries and track items already seen
- **Lists:** to preserve the original order of first appearance
- **Loops:** a nested loop counts how many times each entry repeats
- **String methods:** `strip()`, `lower()`, `split()` and `join()` for normalizing text
- **User input:** a simple menu with a safe default for invalid choices

## Sample Result

For a file containing `apple`, `Banana`, `apple`, `banana`, `Cherry`:

| Mode | Total | Unique | Duplicates |
|---|---|---|---|
| Exact match | 5 | 4 | apple (2 times) |
| Ignore case and spaces | 5 | 3 | apple (2 times), banana (2 times) |

## Edge Cases Covered

- File not found
- Empty file or file with only blank lines
- Blank lines mixed into the data
- Invalid menu option (defaults to exact match)
- No duplicates found (still writes `unique.txt`)

## Limitations and Possible Improvements

- The nested counting loop is O(n²); `collections.Counter` would scale better for large files.
- `unique.txt` is overwritten on every run.
- In ignore-case mode, the saved list contains normalized text rather than the original casing.
- The file name and mode are entered interactively; command-line arguments (e.g. `argparse`) could allow scripting.

## Files

| File | Purpose |
|---|---|
| `find_duplicates.py` | The main program |
| `README.md` | Usage instructions and documentation |
| `summary.md` | This project summary |
| `unique.txt` | Generated output (unique entries) |

## Test Cases

### Test Case 01: Normal Input
<img width="650" alt="Test Case 01" src="https://github.com/user-attachments/assets/3786f131-89bd-481e-8c1c-5fabd4968fb7" />

---

### Test Case 02: Boundary / Minimum Input
<img width="650" alt="Test Case 02" src="https://github.com/user-attachments/assets/b4287d19-39fc-43a6-b218-c13eac7a8519" />

---

### Test Case 03: Invalid Input
<img width="650" alt="Test Case 03" src="https://github.com/user-attachments/assets/f0a74b89-bd4a-40e9-873c-37124f22a5f2" />

---

### Test Case 04: Ignore Case & Extra Spaces
<img width="650" alt="Test Case 04" src="https://github.com/user-attachments/assets/079caeeb-a260-4c73-8cf6-60743de47ef6" />
<img width="459" height="232" alt="image" src="https://github.com/user-attachments/assets/079caeeb-a260-4c73-8cf6-60743de47ef6" />


