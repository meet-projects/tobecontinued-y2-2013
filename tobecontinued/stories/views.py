# Create your views here.
from django.shortcuts import render
from stories.models import Line, Story
from django.http import HttpResponseRedirect

def homePage(request):
    context = {}
    return render(request, 'stories/HomePage.html', context)

def create(request):
    context = {}
    return render(request, 'stories/createstory.html', context)

def submitLine(request, storyID):
    sentence = request.POST['sentence']
    s = Story.objects.filter(id = storyID)
    Line(content = sentence, story = s[0]).save()
    return HttpResponseRedirect('/story/' + str(storyID))

def storyline(request, storyID):
    stories = Story.objects.filter(id = storyID)
    list1 = ['Story Not Found']
    context = {'Lines':list1}
    if stories != []:
        s = stories[0]
	lines = Line.objects.filter(story = stories[0])
    	context={'Lines':lines, 'storyTitle':s.title, 'storyID': str(s.id)}	
    return render(request,'stories/storyline.html',context)


#def clear(request):
  #  s = Story.objects.filter(title = "Sadek the Duck")
  #  Line.objects.filter(story = s[0]).delete()
  #  return HttpResponseRedirect('story')

def newStory(request):
    title1 = request.POST['Title']
    firstLine = request.POST['firstLine']
    new = Story(title = title1)
    new.save()
    Line(content = firstLine, story = new).save()
    return HttpResponseRedirect('/story/' + str(new.id))

#def newStory(request):
  #  newStory = request.POST['newStory']
  #  a=Story(title = newStory)
  #  a.save()
  #  return HttpResponseRedirect('story/' + a.id)
    
def profile(request):
    return render(request, 'stories/profile.html', {})

def signup(request):
    return render(request, 'stories/signuppage.html', {})
