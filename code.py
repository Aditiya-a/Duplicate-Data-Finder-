def find_duplicates():
    # Step 1: Read the file and handle missing file errors (Test Case 3a)
    filename = input("Enter the file name (e.g., data.txt): ").strip()
    
    try:
        with open(filename, 'r') as file:
            # Read lines and strip only the trailing newline character
            raw_lines = [line.rstrip('\n') for line in file.readlines()]
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please enter a valid file name.")
        return

    # Check if the file is empty (Test Case 3b)
    if not raw_lines or all(line.strip() == "" for line in raw_lines):
        print("File is empty. Nothing to check.")
        return

    # Filter out completely blank lines if any exist
    entries = [line for line in raw_lines if line != ""]

    # Step 2: Menu option for matching criteria
    print("\nSelect comparison mode:")
    print("1. Exact match")
    print("2. Ignore case and extra spaces")
    choice = input("Enter option (1 or 2): ").strip()

    if choice == '2':
        # Normalize entries: lowercase and remove leading/trailing & extra inner spaces
        processed_entries = [" ".join(item.lower().split()) for item in entries]
    elif choice == '1':
        processed_entries = entries
    else:
        print("Invalid option selected. Defaulting to Option 1 (Exact match).")
        processed_entries = entries

    # Step 3: Use a set to find unique entries
    # Preserving order for clean display & file saving using a set tracker
    unique_set = set(processed_entries)
    ordered_unique = []
    seen = set()
    for item in processed_entries:
        if item not in seen:
            seen.add(item)
            ordered_unique.append(item)

    total_items = len(processed_entries)
    unique_items = len(unique_set)

    # Step 4: Use a loop to count how many times each entry repeats
    duplicates = []
    for item in ordered_unique:
        count = 0
        for entry in processed_entries:
            if entry == item:
                count += 1
        if count > 1:
            duplicates.append(f"{item} ({count} times)")

    # Step 5: Display results matching the expected test case format
    print(f"\nTotal items: {total_items}  |  Unique items: {unique_items}")

    if duplicates:
        print("Duplicates: " + "  |  ".join(duplicates))
        # Save unique entries to unique.txt
        with open("unique.txt", "w") as out_file:
            for item in ordered_unique:
                out_file.write(item + "\n")
        print("Unique list saved to unique.txt")
    else:
        print("No duplicates found.")
        # Still save the unique list to unique.txt as per project specification
        with open("unique.txt", "w") as out_file:
            for item in ordered_unique:
                out_file.write(item + "\n")


if __name__ == "__main__":
    find_duplicates()