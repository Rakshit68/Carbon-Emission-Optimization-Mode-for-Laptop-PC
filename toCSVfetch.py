import csv

# Open the input text file for reading
with open(r"C:\Users\Rakshit\Desktop\fetch1st.txt", 'r') as file:
    text_data = file.read()

# Split the text data into records based on blank lines
records = [record.strip() for record in text_data.strip().split('\n\n')]

# Initialize a CSV file for writing
with open(r"C:\Users\Rakshit\Desktop\fetch1st.csv", 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write header
    csv_writer.writerow(['NPM', 'PM', 'WS', 'Id', 'ProcessName'])

    # Parse and write each record
    for record in records:
        lines = record.split('\n')
        data = {}
        for line in lines:
            key, value = map(str.strip, line.split(':'))
            data[key] = value
        csv_writer.writerow([data.get('NPM', ''), data.get('PM', ''), data.get('WS', ''), data.get('Id', ''), data.get('ProcessName', '')])

print("CSV file 'process_data.csv' has been created.")
