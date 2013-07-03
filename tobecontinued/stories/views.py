# Create your views here.
from django.shortcuts import render
from stories.models import Line, Story
from django.http import HttpResponseRedirect

def homePage(request):
    context = {}
    return render(request, 'stories/HomePage.html', context)

def submitLine(request):
    sentence = request.POST['sentence']
    s = Story.objects.filter(title__startswith = "Sadek")
    Line(content = sentence, story = s[0]).save()
    return HttpResponseRedirect('story')
<<<<<<< HEAD
    
def storyline(request):
    stories = Story.objects.filter(title = "Sadek the Duck")
    lines = Line.objects.filter(story = stories[0])
    x=len(lines)
    c=lines[x-1]
    context={'stories/storyline':c}
=======

def storyline(request, storyID):
    stories = Story.objects.filter(id = storyID)
    list1 = ['Story Not Found']
    context = {'Lines':list1}
    if stories != []:
	lines = Line.objects.filter(story = stories[0])
    	context={'Lines':lines}	
>>>>>>> d4b107df61f305cc52ba56322dadb65c37db7f32
    return render(request,'stories/storyline.html',context)


def clear(request):
    s = Story.objects.filter(title = "Sadek the Duck")
    Line.objects.filter(story = s[0]).delete()
    return HttpResponseRedirect('story')

def newStory(request):
    newStory = request.POST['newStory']
    a=Story(title = newStory)
    a.save()
    return HttpResponseRedirect('story/' + a.id)
    
