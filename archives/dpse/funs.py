import pandas as pd 
from . import models

def insert(myfile) :
    sheet_names = myfile.sheet_names

    # Loop over each sheet and perform analysis
    for sheet_name in sheet_names:
        # Read the sheet into a dataframe
        df = pd.read_excel(myfile, sheet_name=sheet_name)
        

