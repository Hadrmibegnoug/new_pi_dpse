import pandas as pd 
from .models import *

def cand(sheet_df,year,code):
    sheet_df=replace_nan_with_zero(sheet_df)
   
    # Check the type of sheet based on the sheet name
    if code == "cand1":
        # Insert data into cand1 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            wilaya = row[0]
            effectif = row[1]
            cand1_obj = cand1(annee_scolaire=year, wilaya=wilaya, effectif=effectif)
            cand1_obj.save()

    elif code == "cand2":
        # Insert data into cand2 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            nb1 = row[2]
            nb2 = row[3]
            nb3 = row[4]
            nb4 = row[5]
            nb5 = row[6]
            cand2_obj = cand2(annee_scolaire=year, nb1=nb1, nb2=nb2, nb3=nb3, nb4=nb4, nb5=nb5)
            cand2_obj.save()

    elif code == "cand3":
        # Insert data into cand3 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0 or row.name == 1:
                continue
            serie = row[0]
            nb1   = row[1]
            nb2   = row[2]
            nb3   = row[3]
            nb4   = row[4]
            nb5   = row[5]
            nb6   = row[6]
            nb7   = row[7]
            nb8   = row[8]
            cand3_obj = cand3(annee_scolaire=year,serie=serie, nb1=nb1, nb2=nb2, nb3=nb3, nb4=nb4, nb5=nb5, nb6=nb6, nb7=nb7, nb8=nb8)
            cand3_obj.save()

    elif code == "cand4":
        # Insert data into cand4 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            filiere = row[0]
            nb1 = row[1]
            nb2 = row[2]
            nb3 = row[3]
            nb4 = row[4]
            nb5 = row[5]
            cand4_obj = cand4(filiere=filiere, nb1=nb1,nb2=nb2,nb3=nb3,nb4=nb4,nb5=nb5)
            cand4_obj.save()

    else:
        raise ValueError(f"Unknown sheet type: {code}")



def sort(sheet_df, year, code):
    sheet_df=replace_nan_with_zero(sheet_df)
   
    # Check the type of sheet based on the sheet name
    if code == "sort1":
         for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                institutions = row[0]
                continue
            institutions = row[1]
            nb1   = row[2]
            nb2   = row[3]
            nb3   = row[4]
            nb4   = row[5]
            nb5   = row[6]
            nb6   = row[7]
            nb7   = row[8]
            nb8   = row[9]
            nb9   = row[10]
            nb10  = row[11]
            nb11  = row[12]
            nb12  = row[13]
            nb13  = row[14]
            nb14  = row[15]
            nb15  = row[16]
            nb16  = row[17]
            sort_obj = sort1(annee_scolaire=year,institutions=institutions, nb1=nb1, nb2=nb2, nb3=nb3, nb4=nb4, nb5=nb5, nb6=nb6, nb7=nb7, nb8=nb8, nb9=nb9, nb10=nb10, nb11=nb11, nb12=nb12, nb13=nb13, nb14=nb14, nb15=nb15, nb16=nb16)
            sort_obj.save()
    elif code == "sort2":
        # Insert data into cand4 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            domaine_specilise = row[0]
            nb1 = row[1]
            nb2 = row[2]
            sort_obj2 = sort2(domaine_specilise=domaine_specilise, nb1=nb1,nb2=nb2)
            sort_obj2.save()
    else:
        raise ValueError(f"Unknown sheet type: {code}")
           

            


def ensg(sheet_df, year, code):
    sheet_df=replace_nan_with_zero(sheet_df)
    # Check the type of sheet based on the sheet name
    if code == "ensg1":
        # Insert data into ensg1 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            if row[1]== 0:
                ensg1_obj = ensg1(etablissements=row[0], annee_scolaire=year, nb1=row[2])
            else:
                ensg1_obj = ensg1(etablissements=row[1], annee_scolaire=year, nb1=row[2])

            ensg1_obj.save()

    elif code == "ensg2":
        # Insert data into ensg2 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            ensg2_obj = ensg2(tranche_age=row[0], annee_scolaire=year, nb1=row[1])
            ensg2_obj.save()

    elif code == "ensg3":
        # Insert data into ensg3 table

        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0 or row.name == 1:
                continue
            etablissements = row[0]
            ensg3_obj = ensg3(etablissements=etablissements, annee_scolaire=year,nb1=row[1],nb2=row[2],nb3=row[3],nb4=row[4],nb5=row[5],nb6=row[6],nb7=row[7])
            ensg3_obj.save()

    elif code == "ensg4":
        # Insert data into ensg4 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0 or row.name == 1:
                continue
            etablissements = row[0]
            ensg4_obj = ensg4(etablissements=etablissements, annee_scolaire=year,nb1=row[1],nb2=row[2],nb3=row[3],nb4=row[4],nb5=row[5],nb6=row[6],nb7=row[7],nb8=row[8],nb9=row[9],nb10=row[10],nb11=row[11],nb12=row[12],nb13=row[13],nb14=row[14],nb15=row[15],nb16=row[16],nb17=row[17],nb18=row[18],nb19=row[19])
            ensg4_obj.save()

    elif code == "ensg5":
        # Insert data into ensg5 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            domaine = row[0]
            nb1 = row[1]
            ensg5_obj = ensg5(domaine=domaine, annee_scolaire=year, nb1=nb1)
            ensg5_obj.save()

    elif code == "ensg6":
        # Insert data into ensg6 table
        ins = None
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0 or row.name ==1:
                continue
            if row[1]=="nan":
                etablissements = ins
            else:
                etablissements = row[1]
                ins=row[1]
            ensg6_obj = ensg6(institutions=etablissements, annee_scolaire=year, domaine=row[2],nb1=row[3],nb2=row[4],nb3=row[5],nb4=row[6],nb5=row[7],nb6=row[8],nb7=row[9],nb8=row[10],nb9=row[11],nb10=row[12])
            ensg6_obj.save()

    else:
        raise ValueError(f"Unknown sheet type: {code}")




def replace_nan_with_zero(df):
    """
    Replaces all NaN values in a DataFrame with 0.
    
    Args:
        df (pandas.DataFrame): The DataFrame to modify.
    
    Returns:
        pandas.DataFrame: The modified DataFrame.
    """
    # Use the fillna method to replace all NaN values with 0
    df = df.fillna(0)
    
    return df
