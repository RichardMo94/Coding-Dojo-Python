from django.shortcuts import render, HttpResponse
from time import localtime, timezone, strftime

def index(request):
    return render(request, 'index.html')

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request,'index.html', context)