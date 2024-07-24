
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

# Step 1: Specify the directory containing the CSV files
folder_path = '/Users/anoushkachitnis/Desktop/HVPS data 2'  # Replace with the path to your folder

# Step 2: List all files in the directory
files = os.listdir(folder_path)

# Step 3: Filter out non-CSV files
csv_files = [file for file in files if file.endswith('.csv')]

voltageValsArr = []   #x axis
time = np.array([])
filepathsArr = np.array([])


# Step 4: Read each CSV file into a pandas DataFrame
dataframes = []
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)   #creates a new path for each csv file
    print("Filepath Name: ", file_path)
    filepathsArr = np.append(filepathsArr, file_path) 
    filepathsArr = sorted(filepathsArr)
    
    # ilepathsArr = np.append(filepathsArr, int(file_path[-6:-4]))  #gets the last two indices of the string and converts it into an int
    # filepathsArr = np.sort(filepathsArr)
    
for file in filepathsArr:
    df = pd.read_csv(file, delimiter=';')
    
    #print("DATAFRAMES: ", df)
    
    dataframes.append(df)
    # print(f"Data from file {csv_file}:")
    # print(df.head())  # Display the first few rows of the DataFrame
    # print("\n")
    # print(type(df))
    
    df = df.to_numpy()     #makes the dataframe into a numpy array
    
    print("ITTTT: ", df[0])
    
    str_list = df[0][0].split(',')
    
    
    float_list = [float(x) if x else np.nan for x in str_list]

    float_array = np.array(float_list)
    
    voltageValsArr = np.append(voltageValsArr, float_array[1])
    
    voltageValsArr.sort()
    
print("voltageValsArr: ", voltageValsArr)
    

##############################################

file_path = '/Users/anoushkachitnis/Downloads/HVPS data 2 - SSL - Summer 2024 - Copy of Sheet1.csv'

measuredInputVals = np.array([])

# Open the file and read its contents
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        #print("Each row: ", row)
        measuredInputVals = np.append(measuredInputVals, row[1])
        #print(measuredInputVals)
        
measuredInputVals.sort()
        
        

    
    
    
    
    
   
    
   #  #timeVals = array[:, :, 0]     #it's all the time values for a given voltage
    
    
   #  print("voltage", voltageVals)
   # print("maybe: ", array[:, 1])
   # # print("maybe: ", array[:, 2]) 
   
   #  print("SIZE (im not fat shaming): ", array.shape)
    

   #  csv_string = array[1][0]
   #  print("CSV string: ", csv_string)
    
    # csv_string = df[1][0]
    # # print(csv_string)

    # # Step 1: Split the string into a list of substrings
    # for file in csv_string:
    
    #     str_list = csv_string.split(',')

    #     # print(str_list)

    # # Step 2: Convert each substring to an integer
    #     float_list = [float(x) if x else np.nan for x in str_list]

    #     float_array = np.array(float_list)

    # # Print the resulting list of integers
    #     # print(float_array[0])
    #     # time = np.append(time, float_array[0])
    #     # inputVoltageArr = np.append(inputVoltageArr, float_array[1])
    #     # print("input voltage: ", inputVoltageArr)
        
# print(filepathsArr)
        
        
#print(time)
# print(time.shape)
        
    
    
    #inputVoltageArr.append(voltageVals[0])   #appending the first value of the voltage values
    

    


arr = np.arange(0, 5.1, 0.1)
print("TEST***: ", arr)
print("MeasuredInputVals: ", measuredInputVals)
print(len(arr))
print(len(voltageValsArr))

print(voltageValsArr)

measuredInputVals = measuredInputVals.astype(float)

fig1, ax1 = plt.subplots(nrows=1,figsize=(12,12),sharex=True)
plt.scatter(arr, measuredInputVals,color='b',linewidth=2)
ax1.set_xlabel('Power Source Reading [volts]', fontsize=18)
ax1.set_ylabel('Measured VMON Reading[volts]', fontsize=18)
ax1.grid(True, color="grey", linestyle='--', linewidth=1)
#plt.plot(voltageValsArr, measuredInputVals, color='r')

print(type(arr[1]))
print(type(measuredInputVals[1]))

coefficients = np.polyfit(arr, measuredInputVals, 1)

print(coefficients)

ax1.plot(arr, coefficients[0]*arr + coefficients[1], color = 'r')


# #################

