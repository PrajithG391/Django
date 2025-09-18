from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hoome(request):
    return render(request,'index.html',{'name':'Praju'})

def add(request):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    print(res)


    return render(request, 'result.html', {'result':res})