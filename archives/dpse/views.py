from io import BytesIO
from django.template import loader
from django.http import HttpResponse
import pandas as pd
from .models import *
from django.shortcuts import render
from .forms import UploadFileForm
from .funs import *
import json
from django.core import serializers
def say_hi(request):
    template = loader.get_template('helo.html')
    etudiat_data = {
                        "etu1": list(etu1.objects.all().values()),
                        "etu2": list(etu2.objects.all().values()),
                        "etu3": list(etu3.objects.all().values()),
                        "etu4": list(etu4.objects.all().values()),
                        "etu5": list(etu5.objects.all().values()),
                        "etu6": list(etu6.objects.all().values()),
                        "etu7": list(etu7.objects.all().values()),
                        "etu8": list(etu8.objects.all().values()),
                        "etu9": list(etu9.objects.all().values()),
                        "cand1": list(cand1.objects.all().values()),
                        "cand2": list(cand2.objects.all().values()),
                        "cand3": list(cand3.objects.all().values()),
                        "cand4": list(cand4.objects.all().values()),
                        "ensg1": list(ensg1.objects.all().values()),
                        "ensg2": list(ensg2.objects.all().values()),
                        "ensg3": list(ensg3.objects.all().values()),
                        "ensg4": list(ensg4.objects.all().values()),
                        "ensg5": list(ensg5.objects.all().values()),
                        "ensg6": list(ensg6.objects.all().values()),
                        "bours1": list(bour1.objects.all().values()),
                        "bours2": list(bour2.objects.all().values()),
                        "bours3": list(bour3.objects.all().values()),
                        "transport": list(Transport.objects.all().values()),
                        "EffectifmInstDNG": list(EffectifmInstDNG.objects.all().values()),
                        "Etablissements": list(Etablissements.objects.all().values()),
                        "Etudiants": list(Etudiants.objects.all().values()),
                        # "Cnou":list(Cnou.objects.all().values()),
                        "sort1": list(sort1.objects.all().values()),
                        "sort2": list(sort2.objects.all().values()),
                        "Archives": list(Archives.objects.all().values())
                    }
    
    
    print(etudiat_data)
    etudiat_data_json = json.dumps(etudiat_data)
    context = {'etudiat_data_json': etudiat_data_json}
    return HttpResponse(template.render(context,request))

def upload_file(request):

    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        uploaded_file = request.FILES['file']
        file_contents = uploaded_file.read()

        # Get the sheet names and their corresponding DataFrames
        # excel_data = pd.read_excel(BytesIO(file_contents), sheet_name=None)
        excel_data = pd.read_excel(BytesIO(file_contents), sheet_name=None, engine='xlrd')

        # Get the sheet name and table name from the first sheet
        first_sheet_df = pd.read_excel(BytesIO(file_contents), sheet_name=list(excel_data.keys())[0], header=None)
        sheet_name_col = first_sheet_df.iloc[:, 0]
        table_name_col = first_sheet_df.iloc[:, 2]

        # Insert header and table name into Headertablemap
        
        # Iterate over all sheets and extract headers
        header_df = pd.DataFrame(columns=["Sheet", "Header"])
        for i, sheet_name in enumerate(excel_data):
            if sheet_name == "Feuil1":
                continue
            # Find the row in the first sheet with the matching sheet name and extract the third cell value
            row_index = sheet_name_col[sheet_name_col == sheet_name].index[0]
            value = first_sheet_df.iloc[row_index, 2]
            sheet_df = pd.read_excel(BytesIO(file_contents), sheet_name=sheet_name, header=None)
            header = sheet_df.iloc[0].tolist()
            header_table_map = Headertablemap(header=header, table_name=value)
            header_table_map.save()

            

            # Store the extracted value and header in the header_df DataFrame
            header_df = header_df.append({"Sheet": sheet_name, "Header": header, "Value": value}, ignore_index=True)




            header_table_map = Headertablemap.objects.all()
        return render(request, 'upload.html', {'header_table_map': header_table_map})

    return render(request, 'upload.html')

def insert(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        uploaded_file = request.FILES['file']
        file_contents = uploaded_file.read()

        # Get the sheet names and their corresponding DataFrames
        excel_data = pd.read_excel(BytesIO(file_contents), sheet_name=None)

        # Get the sheet name and table name from the first sheet
        first_sheet_df = pd.read_excel(BytesIO(file_contents), sheet_name=list(excel_data.keys())[0], header=None)
        sheet_name_col = first_sheet_df.iloc[:, 0]
        table_name_col = first_sheet_df.iloc[:, 2]

        # Insert header and table name into Headertablemap
        
        # Iterate over all sheets and extract headers
        header_df = pd.DataFrame(columns=["Sheet", "Header"])
        for i, sheet_name in enumerate(excel_data):
            if sheet_name == "Feuil1":
                continue
            sheet_df = pd.read_excel(BytesIO(file_contents), sheet_name=sheet_name, header=None)
            row_index = sheet_name_col[sheet_name_col == sheet_name].index[0]
            value = first_sheet_df.iloc[row_index, 2]
            if not isinstance(value, str)  :
                continue
            if "cand" in value:
                cand(sheet_df,request.POST['year'],value)
            if "ensg" in value:
                ensg(sheet_df,request.POST['year'],value)
            if "sort" in value:
                sort(sheet_df,request.POST['year'],value)
            # if "Cnou" in value:
            #     sort(sheet_df,request.POST['year'],value)
            

            

            # Store the extracted value and header in the header_df DataFrame
            




            header_table_map = Headertablemap.objects.all()
        return render(request, 'upload.html', {'header_table_map': header_table_map})

    return render(request, 'upload.html')
