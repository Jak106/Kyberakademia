import csv

# Load the MFT CSV file
input_file = "filtered_mft.csv"  # Change this to the correct file path
output_file = "filtered_mft_2.csv"

# Open the input and output files
with open(input_file, "r", encoding="utf-8", errors="ignore") as infile, open(output_file, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Read the header
    header = next(reader)
    writer.writerow(header)
    
    # Get column indices
    try:
        created0x10_index = header.index("Created0x10")
        created0x30_index = header.index("Created0x30")
        filename_index = header.index("FileName")
    except ValueError as e:
        raise ValueError("Missing required columns in the CSV file")
    
    # Filter out rows where both Created0x10 and Created0x30 are empty, and check for Flag pattern in filename
    filtered_count = 0
    for row in reader:
        if (row[created0x10_index] or row[created0x30_index]) and "Flag{" in row[filename_index]:
            writer.writerow(row)
            filtered_count += 1

print(f"Filtered MFT saved to {output_file}. {filtered_count} entries contain a flag.")

