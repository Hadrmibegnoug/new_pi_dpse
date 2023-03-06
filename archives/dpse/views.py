from io import BytesIO
from django.template import loader
from django.http import HttpResponse
import pandas as pd
from .models import *
from django.shortcuts import render
from .forms import UploadFileForm
from .funs import *
def say_hi(request):
    template = loader.get_template('helo.html')
    etudiat_data={"etu1":cand1.objects.all().values(),"etu2":etu2.objects.all().values(),
                  "etu3":etu3.objects.all().values(),"etu4":etu4.objects.all().values(),
                  "etu5":etu5.objects.all().values(),"etu6":etu6.objects.all().values(),
                  "etu7":etu7.objects.all().values(),"etu8":etu8.objects.all().values(),
                  "etu9":etu9.objects.all().values()}
    print(etudiat_data)
    return HttpResponse(template.render(etudiat_data,request))

def upload_file(request):

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

            

            # Store the extracted value and header in the header_df DataFrame
            




            header_table_map = Headertablemap.objects.all()
        return render(request, 'upload.html', {'header_table_map': header_table_map})

    return render(request, 'upload.html')
