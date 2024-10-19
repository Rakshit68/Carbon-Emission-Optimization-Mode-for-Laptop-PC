import csv

# Define empty lists to store data from the CSV file
process_name = []
factor = []
base_priority = []



#defining all power consumption components
cpu_watts=[['core-i3',18.83],
                 ['core-i5',20],
                 ['core-i7',28.58],
                 ['core-i9',33],
                 ['ryzen-3',15],
                 ['ryzen-5',18],
                 ['ryzen-7',26.36],
                 ['ryzen-9',31]]
gpu_watts=[['gtx-1650',75],
                 ['gtx-1650ti',65],
                 ['gtx-1660',90],
                 ['gtx-1660ti',75],
                 ['rtx-3050',55],
                 ['rtx-3050ti',65],
                 ['rtx-3060',105],
                 ['rtx-3070',115]]
ram_watts=[['ddr4-8gb',2.5],
                 ['ddr4-16gb',5],
                 ['ddr3-8gb',3],
                 ['ddr3-16gb',6],
                 ['ddr2-4gb',4],
                 ['ddr2-8gb',8],
                 ['ddr1-4gb',5],
                 ['ddr1-8gb',10]]
storage_watts=[['512gb-hdd',4],
               ['1tb-hdd',3.5],
               ['256bg-ssd',1.875],
               ['512gb-ssd',1.625],
               ['1tb-ssd',3]]
motherboard_watts=[['regular',24.6],['high-end',46.5]]


#assuming a laptop with ryzen-5,rtx-3050,8gb-ddr4,1tb-ssd and regular motherboard
laptop_watts=cpu_watts[5][1]+gpu_watts[4][1]+ram_watts[0][1]+storage_watts[4][1]+motherboard_watts[0][1]



#defining future required entities
posi_list=[]
name_list=[]
factor_usage=[]

high_priority=[13,14,15,16]
medium_priority=[8,9,10,11,12]
low_priority=[5,6,7]
idle_processes=[1,2,3,4]

# Specify the path to your CSV file
csv_file_path = "C:/Users/Rakshit/Desktop/setVal.csv"

# Open and read the CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Check if the row has at least four columns
        if len(row) >= 4:
            # Append the first column (index 0) to the first_column list
            process_name.append(row[0])
            # Append the third column (index 2) to the third_column list
            factor.append(row[2])
            # Append the fourth column (index 3) to the fourth_column list
            base_priority.append(int(row[3]))

#Converting the value of private_bytes to pure integer
for element in factor:
    temp=float(element)
    factor_usage.append(temp)
column_sum=sum(factor_usage)
#Removing duplicate entries of processes and merging them into one and also merging their ram usage

#Getting positions of each process
def find_positions(input_list):
    positions = {}
    
    for i, item in enumerate(input_list):
        if item not in positions:
            positions[item] = []
        positions[item].append(i)
    
    return [(key, list(value)) for key, value in positions.items()]

# usage:
element_positions = find_positions(process_name)

#Creating a dictionary with k,v pair as name of process,total factor used by the process
new_dict={}
s=0
for tup in element_positions:
    v=tup[1]
    k=tup[0]
    for lis in v:
        s=s+factor_usage[lis]
    new_dict[k]=s
    s=0
#print(new_dict)

#Creating a dictionary with k,v pair as name of process,priority provided by sysinternal suite
new_dict2={}
count=0
s2=0
for tup in element_positions:
    v2=tup[1]
    k2=tup[0]
    for lis in v2:
        count+=1
        s2=s2+base_priority[lis]
    avg=int(s2/count)
    new_dict2[k2]=avg
    s2,count=0,0
#print(new_dict2)

'''
column_number = 2  # Replace with the actual 0-based column number


# Initialize a variable to store the sum
column_sum = 0


# Open the CSV file for reading
with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV file
    for row in reader:
        try:
            # Try to convert the column value to a numeric type (e.g., float)
            column_value = float(row[column_number])

            
            # Add the numeric value to the sum
            column_sum += column_value
        except ValueError:
            # Handle non-numeric values (you can skip or log these values)
            pass
'''

#Creating a dictionary with k,v pair as name of process,total memory used by the process in %
new_dict3={}
for k,v in new_dict.items():
    new_dict3[k]=(v/column_sum)*100
#print(new_dict3)


#power usage in % per process
new_dict4={}
for k,v in new_dict3.items():
    new_dict4[k]=(v/100)*laptop_watts
#print(new_dict4)

#Writing details in a csv file
output_file = r"C:\Users\Rakshit\Desktop\FinalOutput.csv"
with open(output_file, "w", newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['Process Name', 'Factor', '(%)Power usage','Approx. power usage in wh','Priority type'])
    for (k1, v1), (k2, v2),(k3,v3),(k4,v4) in zip(new_dict.items(), new_dict3.items(), new_dict2.items(),new_dict4.items()):
        if v3 in high_priority:
            writer.writerow([k1, v1, v2, v4, 'High'])
        elif v3 in medium_priority:
            writer.writerow([k1, v1, v2, v4, 'Medium'])
        elif v3 in low_priority:
            writer.writerow([k1, v1, v2, v4, 'Low'])
        elif v3 in idle_processes:
            writer.writerow([k1, v1, v2, v4, 'Idle'])
        else:
            writer.writerow([k1, v1, v2, v4, 'Extreme'])

#Extracting the idle apps to text file
output_f = "C:/Users/Rakshit/Desktop/Idle_Apps.txt"
with open(output_f, "w", newline="") as out_file:
    for k,v in new_dict2.items():
        if k in idle_processes:
            out_file.write(k)
            out_file.write("\n")
        else:
            continue
out_file.close()
print("Files have been written successfully!.............")