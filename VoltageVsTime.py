import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from random import randint

COLORS = []



# Step 1: Specify the directory containing the CSV files
folder_path = '/Users/anoushkachitnis/Desktop/HVPS data 2'  # Replace with the path to your folder

# Step 2: List all files in the directory
files = os.listdir(folder_path)

# Step 3: Filter out non-CSV files
csv_files = [file for file in files if file.endswith('.csv')]


filepathsArr = np.array([])






arr = np.arange(0, 5.1, 0.1)
print("TEST***: ", arr)
print(len(arr))


fig1, ax1 = plt.subplots(nrows=1,figsize=(16,24),sharex=True)
ax1.set_xlabel('Time', fontsize=18)
ax1.set_ylabel('Output Voltage [volts]', fontsize=18)





# Step 4: Read each CSV file into a pandas DataFrame
dataframes = []
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)   #creates a new path for each csv file
    print("Filepath Name: ", file_path)
    filepathsArr = np.append(filepathsArr, file_path) 
    filepathsArr = sorted(filepathsArr)
    
    # ilepathsArr = np.append(filepathsArr, int(file_path[-6:-4]))  #gets the last two indices of the string and converts it into an int
    # filepathsArr = np.sort(filepathsArr)
    
for index, file in enumerate(filepathsArr):
    
    voltageValsArr = []   #resets after every file
    time = np.array([])

    df = pd.read_csv(file, delimiter=';')
    
    #print("DATAFRAMES: ", df)
    
    dataframes.append(df)
    # print(f"Data from file {csv_file}:")
    # print(df.head())  # Display the first few rows of the DataFrame
    # print("\n")
    # print(type(df))
    
    df = df.to_numpy()     #makes the dataframe into a numpy array
    
    print(df[:, 0].shape)
    
    
    #print("ITTTT: ", df[0])
    
    volts = df[:, 0]
    
    print("volts: ", volts)
    
    for volt in volts:
        
        print("VOLT: ", volt)
        
        str_list = volt.split(',')
        
        
        float_list = [float(x) if x else np.nan for x in str_list]
    
        float_array = np.array(float_list)
        
        voltageValsArr = np.append(voltageValsArr, float_array[1])
        time = np.append(time, float_array[0])
        
        # print("***************************************")
        # print(voltageValsArr)
        # print(time)
        # print("***************************************")
        
    for i in range(len(time)):
        COLORS.append('#%06X' % randint(0, 0xFFFFFF))
        
        
    plt.plot(np.arange(len(time)), voltageValsArr,  color=COLORS[index], linewidth=2, alpha = 0.5)
    # plt.scatter(np.arange(len(time)), voltageValsArr, cmap='rainbow', linewidth=2, alpha = 0.5)
        
    
print(voltageValsArr)
print(time)


values = np.linspace(0, 1, 51)

# Get a list of 51 distinct colors from the 'tab10' colormap
colors = plt.cm.tab10(values)

print("COLORS*****: ", colors)
print(len(colors))

time = np.arange(len(time))



    
    



# arr = np.arange(0, 5.1, 0.1)
# print("TEST***: ", arr)
# print(len(arr))
# print(len(voltageValsArr))

# fig1, ax1 = plt.subplots(nrows=1,figsize=(8,8),sharex=True)
# plt.scatter(time,voltageValsArr,color=colors,linewidth=2)
# ax1.set_xlabel('Time [seconds]', fontsize=18)
# ax1.set_ylabel('Output Voltage [volts]', fontsize=18)

# ax1.grid(True, color="grey", linestyle='--', linewidth=1)







#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:58:45 2024

@author: anoushkachitnis
"""