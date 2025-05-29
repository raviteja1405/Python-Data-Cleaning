import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random


def data_cleaning_master(data_path,data_name):
    
    print("Thankyou for giving the deails.")
     
    sec=random.randint(1,4)

    print(f"pls wait for {sec} second.while checking the path")
    time.sleep(sec)

    #checking if the path exists
    if not os.path.exists(data_path):
        print("please enter correct path...")
        return
    else:
        if data_path.endswith('.csv'):
            print("dataset is csv.")
            data=pd.read_csv(data_path,encoding_errors="ignore")

        elif data_path.endswith('.xlsx'):
            print("dataset is excel file.")
            data=pd.read_excel(data_path)

        else:
            print("Unknown file type")
            return
        
    print(f"pls wait for {sec}seconds.while checking total columns and rows.")
    time.sleep(sec)

    #showing number of records
    print(f"Dataset contain total rows:{data.shape[0]},Total columns:{data.shape[1]}")

    print(f"pls wait for {sec}seconds.while checking duplicates.")
    time.sleep(sec)

    # checking duplicates
    duplicates = data.duplicated()
    total_duplicate=duplicates.sum()
    print(f'Datasets has total duplicates records:{total_duplicate}')

    print(f"pls wait for {sec}seconds.while saving total duplicates.")
    time.sleep(sec)

    # saving duplicates
    if total_duplicate>0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f"{data_name}_duplicates.csv",index=None)

    # deleting duplicates
    df = data.drop_duplicates()

    print(f"pls wait for {sec}seconds.while checking missing values.")
    time.sleep(sec)

    # find missing values
    total_missing_values = df.isnull().sum().sum()
    missing_value_by_columns = df.isnull().sum()

    print(f"Dataset has total missing value:{total_missing_values}")
    print(f"Dataset has total missing value by column:\n {missing_value_by_columns}")


    # dealing with missing values
    #fillna --int and float
    #dropna --any object
    
    print(f"pls wait for {sec}seconds.while cleaning dataset.")
    time.sleep(sec)

    columns = df.columns
    for col in columns:
        if df[col].dtype in (float,int):
            df[col] = df[col].fillna(df[col].mean())
        else:
            #dropping all rows with missing records
            df.dropna(subset=col,inplace=True) 

    print(f"pls wait for {sec}seconds.while exporting dataset.")
    time.sleep(sec)

    # data is cleaned
    print(f"congrats! Dataset is cleaned! \n number of rows:{df.shape[0]} number of columns:{df.shape[1]}")

    # saving the dataset
    df.to_csv(f'{data_name}_cleaned_data.csv',index=None)
    print("Dataset is saved.")

if __name__=="__main__":
    print("Welcome to data cleaning process.")
    data_path=input("please enter dataset path:")
    data_name=input("please enter dataset name:")

    # calling the function
data_cleaning_master(data_path,data_name)
