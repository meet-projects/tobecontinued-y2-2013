# Create your views here.
from django.shortcuts import render
from stories.models import Line, Story

def homePage(request):
    context = {}
    return render(request, 'stories/HomePage.html', context)

def submitLine(request):
    sentence = request.POST['sentence']
    s = Story.objects.filter(title__startswith = "Sadek")
    Line(content = sentence, story = s[0]).save()
    return HttpResponseRedirect('story')
    
def storyline(request):
    context={}
    return render(request,'stories/storyline.html',context)
