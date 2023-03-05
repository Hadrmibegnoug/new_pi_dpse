# import pandas as pd 
from models import *

def cand(sheet_df,year,code):
   
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


def ensg(sheet_df, year, code):
    # Check the type of sheet based on the sheet name
    if code == "ensg1":
        # Insert data into ensg1 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            ensg1_obj = ensg1(etablissements=row[0], annee_scolaire=year, nb1=row[1])
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
            if row.name == 0:
                continue
            etablissements = row[0]
            niveau = row[1]
            nb1 = row[2]
            ensg3_obj = ensg3(etablissements=etablissements, annee_scolaire=year, niveau=niveau, nb1=nb1)
            ensg3_obj.save()

    elif code == "ensg4":
        # Insert data into ensg4 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            etablissements = row[0]
            nb1 = row[1]
            nb2 = row[2]
            ensg4_obj = ensg4(etablissements=etablissements, annee_scolaire=year, nb1=nb1, nb2=nb2)
            ensg4_obj.save()

    elif code == "ensg5":
        # Insert data into ensg5 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            niveau = row[0]
            nb1 = row[1]
            ensg5_obj = ensg5(niveau=niveau, annee_scolaire=year, nb1=nb1)
            ensg5_obj.save()

    elif code == "ensg6":
        # Insert data into ensg6 table
        for _, row in sheet_df.iterrows():
            # Skip the first row since it contains the sheet name and year
            if row.name == 0:
                continue
            etablissements = row[0]
            nb1 = row[1]
            nb2 = row[2]
            ensg6_obj = ensg6(etablissements=etablissements, annee_scolaire=year, nb1=nb1, nb2=nb2)
            ensg6_obj.save()

    else:
        raise ValueError(f"Unknown sheet type: {code}")

