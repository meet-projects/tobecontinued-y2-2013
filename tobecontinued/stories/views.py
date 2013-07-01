# Create your views here.
from django.shortcuts import render

def homePage(request):
    context = {}
    return render(request, 'stories/HomePage.html', context)

def submitLine(request):
    
