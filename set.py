import csv

# Define the input CSV file and output CSV file paths
input_file_path = r"C:\Users\Rakshit\Desktop\merged.csv"
output_file_path = r"C:\Users\Rakshit\Desktop\setVal.csv"

# Function to calculate the factor based on input values
def calculate_factor(col1_value, col2_value, col3_value):
    # Replace this with your own formula for calculating the factor
    factor = (col1_value * col3_value) / col2_value
    return factor

# Read the input CSV file
with open(input_file_path, mode='r', newline='') as input_file:
    reader = csv.DictReader(input_file)
    
    # Create a list to store rows for the output CSV
    output_rows = []

    for row in reader:
        # Extract values for the necessary columns
        process_name = row["ProcessName"]
        id_value = row["Id"]
        priority = row["Priority"]

        # Convert the values to float if they are numeric
        try:
            col1_value = float(row["NPM"])
            col2_value = float(row["PM"])
            col3_value = float(row["WS"])

            # Calculate the factor using the custom function
            factor = calculate_factor(col1_value, col2_value, col3_value)

            # Append the calculated values to the output rows
            output_rows.append([process_name, id_value, factor, priority])
        except ValueError:
            # Skip rows with non-numeric values
            pass

# Write the output rows to the output CSV file without a header
with open(output_file_path, mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(output_rows)  # Write the data rows

print("Factor calculation completed and saved to 'setVal.csv' without a header.")
