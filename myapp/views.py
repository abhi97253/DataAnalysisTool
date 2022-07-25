from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json
from .models import Data

def hello (request):
    if(request.method=='POST'):
        pre_data=Data.objects.all()
        pre_data.delete()

        file=request.FILES['file']
        df=pd.read_csv(file)
        json_records=df.reset_index().to_json(orient='records')
        data=[]
        data=json.loads(json_records)
        for d in data:
            name=d['property_name']
            price=d['property_price']
            rent=d['property_rent']
            emi=d['emi']
            tax=d['tax']
            other_exp=d['other_exp']
            monthly_exp=tax+emi+other_exp
            monthly_inc=rent-monthly_exp
            dt=Data(name=name,price=price,rent=rent,emi=emi,tax=tax,other_exp=other_exp,monthly_exp=monthly_exp
            ,monthly_inc=monthly_inc)
            dt.save()
        data_objects=Data.objects.all()
        context={'data_objects':data_objects}
        return render (request,'myapp/index.html',context)

    else:
        print("this is get method")

    return render (request,'myapp/index.html')


