import csv

# Function to split a line into cells based on spaces and tabs
def split_line(line):
    cells = []
    current_cell = ""
    in_word = False

    for char in line:
        if char.isspace():
            if in_word:
                cells.append(current_cell)
                current_cell = ""
            in_word = False
        else:
            current_cell += char
            in_word = True

    # Append the last cell if there is one
    if current_cell:
        cells.append(current_cell)

    # Reconstruct cells to combine words separated by up to 5 spaces
    reconstructed_cells = []
    i = 0
    while i < len(cells):
        current_word = cells[i]
        j = i + 1
        while j < len(cells) and not cells[j][0].isdigit() and j - i <= 5:
            current_word += " " + cells[j]
            j += 1
        i = j
        reconstructed_cells.append(current_word)

    return reconstructed_cells

# Input and output file names
input_file = "C:/Users/Rakshit/Desktop/Registry.txt"
output_file = "C:/Users/Rakshit/Desktop/outputCSV.csv"

# Read the input file and write to the CSV file
with open(input_file, "r") as in_file, open(output_file, "w", newline="") as out_file:
    csv_writer = csv.writer(out_file)

    # Read the first line (header) but do not process it
    next(in_file)

    for line in in_file:
        # Split the line into cells based on spaces and tabs, combining words separated by up to 5 spaces
        cells = split_line(line)

        # Write the cells to the CSV file
        csv_writer.writerow(cells)

print(f"Conversion from {input_file} to {output_file} complete.")
