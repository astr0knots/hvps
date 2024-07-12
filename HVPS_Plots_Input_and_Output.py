import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Specify the directory containing the CSV files
folder_path = '/Users/anoushkachitnis/Desktop/HVPS testing data'  # Replace with the path to your folder

# Step 2: List all files in the directory
files = os.listdir(folder_path)

# Step 3: Filter out non-CSV files
csv_files = [file for file in files if file.endswith('.csv')]

inputVoltageArr= []   #x axis
stdArr = []           #y axis

# Step 4: Read each CSV file into a pandas DataFrame
dataframes = []


for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)   #creates a new path for each csv file
    df = pd.read_csv(file_path)
    
    print("DATAFRAMES: ", df)
    
    dataframes.append(df)
    print(f"Data from file {csv_file}:")
    print(df.head())  # Display the first few rows of the DataFrame
    print("\n")
    print(type(df))
    
    array = df.to_numpy()     #makes the dataframe into a numpy array
    
    voltageVals = array[:, 0]  
    
    
    
    
    print("voltage", voltageVals)
    
    std = np.std(voltageVals)
    stdArr.append(std)
    
    print("Standard Deviation: ", std)
    
    
    
    inputVoltageArr.append(voltageVals[0])   #appending the first value of the voltage values
    


stdArr = np.array(stdArr)

arr = np.arange(0, 5.1, 0.1)
print("TEST***: ", arr)
print(len(arr))


#################


def Output2Input(output):
    return output/120

def Inp2Out(inp):
    return inp*120
    




fig1, ax1 = plt.subplots(nrows=1,figsize=(8,8),sharex=True)
plt.scatter(inputVoltageArr,stdArr,color='k',linewidth=2)

secax = ax1.secondary_xaxis('top', functions=(Output2Input, Inp2Out))
secax.set_xlabel('Input Voltage [volts]', fontsize = 18)

#ax2.scatter(arr, stdArr, color='r', linewidth=2)
ax1.set_xlabel('Output Voltage [volts]', fontsize=18)
ax1.set_ylabel('Standard Deviation [volts]', fontsize=18)

#ax2.set_xlabel('Input Voltage [volts]', fontsize=18)

ax1.grid(True, color="grey", linestyle='--', linewidth=1)

print(stdArr)





