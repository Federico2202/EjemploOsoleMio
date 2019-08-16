from django.shortcuts import render
from django.http import HttpRequest

def mivista(request):
    return render(request,'OsoleMioApp/index.html')
