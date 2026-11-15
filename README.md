# Duplicate Finder

A simple Python command-line tool that reads a text file, finds duplicate lines, and saves a de-duplicated list to `unique.txt`.

## Features

- Reads any plain-text file (one entry per line)
- Two comparison modes:
  1. **Exact match** – lines must be identical
  2. **Ignore case and extra spaces** – `"Hello  World"` and `"hello world"` count as the same entry
- Reports the total number of items and the number of unique items
- Lists each duplicated entry along with how many times it appears
- Saves the unique entries (in original order) to `unique.txt`
- Handles a missing file and an empty file with clear messages

## Requirements

- Python 3.6 or newer (uses f-strings)
- No external libraries

## Usage

1. Save the script as `find_duplicates.py`.
2. Put the file you want to check in the same folder (or use its full path).
3. Run:

   ```bash
   python find_duplicates.py
   ```

4. Enter the file name when prompted, then choose a comparison mode.

## Example

**Input file (`data.txt`):**

```
apple
Banana
apple
banana
Cherry
```

**Option 1 – Exact match:**

```
Total items: 5  |  Unique items: 4
Duplicates: apple (2 times)
Unique list saved to unique.txt
```

**Option 2 – Ignore case and extra spaces:**

```
Total items: 5  |  Unique items: 3
Duplicates: apple (2 times)  |  banana (2 times)
Unique list saved to unique.txt
```

## Output

- **Console:** summary of total items, unique items, and duplicates with counts.
- **`unique.txt`:** each unique entry on its own line, in order of first appearance. In option 2, entries are saved in their normalized (lowercase, single-spaced) form.

## Edge Cases

| Situation | Behavior |
|---|---|
| File not found | Prints an error message and exits |
| File empty or only blank lines | Prints "File is empty. Nothing to check." and exits |
| Blank lines in the file | Ignored |
| Invalid menu choice | Defaults to Option 1 (Exact match) |
| No duplicates | Prints "No duplicates found." and still writes `unique.txt` |

## How It Works

1. Reads the file and removes trailing newlines.
2. Applies the chosen comparison mode (optionally normalizing case and spacing).
3. Uses a `set` to count unique items and a list to preserve their original order.
4. Loops through the entries to count how many times each repeats.
5. Prints the results and writes `unique.txt`.

## Notes

- `unique.txt` is overwritten each time the program runs.
- Counting uses a nested loop for clarity; for very large files, `collections.Counter` would be faster.