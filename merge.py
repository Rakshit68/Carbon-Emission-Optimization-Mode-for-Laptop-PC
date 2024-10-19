import csv

# Function to read a CSV file into a dictionary
def read_csv_to_dict(file_path, key_column):
    data_dict = {}
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = row[key_column]
            data_dict[key] = row
    return data_dict

# Function to merge two dictionaries based on a common key
def merge_dicts(dict1, dict2):
    merged_dict = {}
    for key in set(dict1.keys()) & set(dict2.keys()):
        merged_dict[key] = {**dict1[key], **dict2[key]}
    return merged_dict

# Define the file paths and key column
file1_path = r"C:\Users\Rakshit\Desktop\fetch1st.csv"
file2_path = r"C:\Users\Rakshit\Desktop\cmd_output.csv"
key_column = 'Id'

# Read CSV files into dictionaries
data_dict1 = read_csv_to_dict(file1_path, key_column)
data_dict2 = read_csv_to_dict(file2_path, key_column)

# Merge the dictionaries
merged_data = merge_dicts(data_dict1, data_dict2)

# Get the fieldnames from the first dictionary (assuming it contains all the fields you need)
fieldnames = list(data_dict1[next(iter(data_dict1.keys()))].keys())

# Ensure "Priority" is in fieldnames
if "Priority" not in fieldnames:
    fieldnames.append("Priority")

# Write the merged data to a new CSV file
merged_file_path = r"C:\Users\Rakshit\Desktop\merged.csv"
with open(merged_file_path, mode='w', newline='') as merged_file:
    writer = csv.DictWriter(merged_file, fieldnames=fieldnames)
    writer.writeheader()
    for key in merged_data:
        # Set "Priority" to 6 if missing
        if "Priority" not in merged_data[key]:
            merged_data[key]["Priority"] = 6
        writer.writerow(merged_data[key])

print("CSV files have been merged and saved as 'merged.csv'.")
