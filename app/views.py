from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='This data is our assumption'
    d={'assimption':data}
    return render(request,'data_render.html',context=d)

def login(request):
    d={'username':'pavani','age': 22}
    return render(request,'login.html',context=d)