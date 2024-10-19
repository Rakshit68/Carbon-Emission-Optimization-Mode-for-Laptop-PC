import pandas as pd

# Define the function to normalize CO2 emissions (you can replace this with your own function)
def normalize_co2(value, column_list):
    value = float(value)
    max_c = max(column_list)  # Use the previously calculated maximum value
    min_c = min(column_list)  # Use the previously calculated minimum value
    # Your normalization logic goes here
    temp = (value - min_c) / (max_c - min_c)
    # For example, if you want to double the value:
    return float(temp)

# Input CSV file and output CSV file paths
input_file = r"C:\Users\Rakshit\Desktop\Final.csv"
output_file = r"C:\Users\Rakshit\Desktop\output.csv"

# Read the input CSV file
df = pd.read_csv(input_file)

# Make a copy of the dataframe
df_copy = df.copy()

# Get the values from the 'Carbon emission' column to pass to the normalize_co2 function
column_list = df['Carbon emission'].tolist()

# Process the 'Carbon emission' column using the normalize_co2 function and store it as a new column
df_copy['Normalized Co2E'] = df_copy['Carbon emission'].apply(lambda x: normalize_co2(x, column_list))

# Save the modified dataframe to a new CSV file
df_copy.to_csv(output_file, index=False)

print("CSV file processing complete. Output saved to", output_file)
