from io import BytesIO
from django.template import loader
from django.http import HttpResponse
import pandas as pd
from .models import Headertablemap,etu1,etu2,etu3,etu4,etu5,etu6,etu7,etu8,etu9
from django.shortcuts import render
from .forms import UploadFileForm
from .funs import *
def index(request):
    template = loader.get_template('helo.html')
    e1=etu1.objects.all().values()
    e2=etu2.objects.all().values()
    e3=etu3.objects.all().values()
    e4=etu4.objects.all().values()
    e5=etu5.objects.all().values()
    e6=etu6.objects.all().values()
    e7=etu7.objects.all().values()
    e8=etu8.objects.all().values()
    e9=etu9.objects.all().values()
    etudiat_data={"etu1":e1,"etu2":e2,"etu3":e3,"etu4":e4,"etu5":e5,"etu6":e6,"etu7":e7,"etu8":e8,"etu9":e9}
    return HttpResponse(template.render(etudiat_data,request))
def say_hi(request):
    return render(request,'helo.html')

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


