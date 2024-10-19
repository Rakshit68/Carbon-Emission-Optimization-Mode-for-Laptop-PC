import csv

# Function to read data from a text file and convert it to a CSV file
def text_to_csv(input_file, output_file, delimiter='\t'):
    try:
        with open(input_file, 'r', encoding='utf-8') as txtfile:
            # Read the lines from the text file
            lines = txtfile.readlines()

            # Remove leading and trailing whitespace from each line and split into columns
            data = [line.strip().split(delimiter) for line in lines]

            # Specify the CSV file mode and write the data
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                # Write the data to the CSV file
                csv_writer.writerows(data)

        print(f"Conversion from {input_file} to {output_file} is successful.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = input("Enter the input text file name: ")
    output_file = input("Enter the output CSV file name: ")
    delimiter = input("Enter the delimiter (default is tab, press Enter to use default): ")

    if delimiter == '':
        delimiter = '\t'

    text_to_csv(input_file, output_file, delimiter)
``
