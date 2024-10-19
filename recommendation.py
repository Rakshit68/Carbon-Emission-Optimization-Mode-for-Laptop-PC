import csv

# Initialize an empty dictionary to store the data
data_dict = {}

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = r"C:\Users\Rakshit\Desktop\output.csv"

# Declare the scale factor and threshold
scale_factor = 1.5
total_normalized_co2e = 0 # Initialize the total normalized co2e to calculate the threshold
c_mode= 0.6 

try:
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        
        # Skip the header row if it exists
        next(reader, None)
        
        for row in reader:
            if len(row) >= 5:  # Ensure the row has at least 5 columns
                application = row[0]  # 1st column (Applications)
                priority = row[2]     # 3rd column (Priority)
                co2e = float(row[4]) # 5th column (Normalized Co2E), converted to a float
                
                # Calculate the total normalized co2e
                total_normalized_co2e += co2e
                
                # Check if the application already exists in the dictionary
                if application in data_dict:
                    data_dict[application].append([priority, co2e])
                else:
                    data_dict[application] = [[priority, co2e]]

    # Calculate the threshold as 60% of the total normalized co2e
    threshold = c_mode * total_normalized_co2e
    

    # Create a dictionary to store the scores for each application
    score_dict = {}
    
    for application, values in data_dict.items():
        score = 0
        for priority, co2e in values:
            if priority == 'High':
                score += 1 * co2e
            elif priority == 'Medium':
                score += 1.5 * co2e
            elif priority == 'Low':
                score += 1.5 * 1.5 * co2e
        
        # Add the application and its score to the score_dict
        score_dict[application] = score

    # Sort applications in descending order of scores
    sorted_applications = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)


    # Create a recommendation list
    recommendation_list = []
    remaining_co2e = total_normalized_co2e  # Initialize with the total CO2E  
    for application, score in sorted_applications:
        # Check if adding this application's CO2E exceeds the threshold
        if remaining_co2e >= threshold:
            recommendation_list.append(application)
            remaining_co2e -= data_dict[application][0][1]


    # Print the recommendation list
    '''print("\nRecommendation List:")
    for app in recommendation_list:
        print(app)'''
    
    file_path = r"C:\Users\Rakshit\Desktop\Recommendations.txt"

    # Open the file in write mode ('w')
    with open(file_path, 'w') as file:
        # Iterate through the list and write each item to a new line in the file
        for item in recommendation_list:
            file.write(item + '\n')

    file.close()


except FileNotFoundError:
    print(f"File '{csv_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Now recommendation_list contains the recommended applications
