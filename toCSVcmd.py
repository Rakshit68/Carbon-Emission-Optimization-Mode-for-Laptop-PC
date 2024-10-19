import csv

# Read the input text file
with open(r"C:\Users\Rakshit\Desktop\cmd_output.txt", 'r') as file:
    lines = file.readlines()

# Initialize a CSV file for writing
with open(r"C:\Users\Rakshit\Desktop\cmd_output.csv", 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(['Priority', 'Id'])

    # Process each line in the input file
    for line in lines[2:]:
        # Split the line into columns based on whitespace
        columns = line.split()

        # Check if there are exactly 3 columns (Caption, Priority, ProcessId)
        if len(columns) == 3:
            _, priority, process_id = columns
            csv_writer.writerow([priority, process_id])

print("CSV file 'process_data.csv' has been created without the 'Caption' column.")
