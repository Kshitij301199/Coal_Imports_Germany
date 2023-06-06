import os
import argparse
import numpy as np
import pandas as pd

def clean_data(filename:str) -> None:
    """
    Cleans the excel file entered.
    For this dataset, converts '-' to 0 and '.' to np.nan
    """
    filepath = os.path.join("../data/",str(filename))
    data = pd.read_excel(filepath,sheet_name="Sheet1")
    destination = "../data/CleanedData.csv"
    data.columns = [c.strip().replace(" ","_") for c in data.columns.values.tolist()]
    data = data.replace({"-":0,".":np.nan})
    print(f"File taken from {filepath}. File saved at {destination}")
    data.to_csv(destination)

def main() -> None:
    # cwd = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--filename", type=str, required=True, help="Enter the filename here")
    parser_dict = parser.parse_args()
    clean_data(parser_dict.filename)
    # print(parser_dict) 

if __name__ == "__main__":
    main()