from django.shortcuts import render
from stories.models import Line, Story
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def homePage(request):
    context = {}
    return render(request, 'stories/HomePage.html', context)

def logIn(request):
    username1 = request.POST['username']
    password2 = request.POST['password']
    user = authenticate(username = username1, password = password2)
    if user is not None:
	login (request, user)
        return HttpResponseRedirect('profile')
    else:
	return HttpResponseRedirect('home')
    

def createUser(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['Email']
    userName = request.POST['UserName']
    password = request.POST['Password']
    User.objects.create_user(username = userName, email = email, password = password, first_name = firstname, last_name = lastname)
    #username1 = request.POST['username']
    #password2 = request.POST['password']
    user = authenticate(username = userName, password = password)
    if user is not None:
	login (request, user)
        return HttpResponseRedirect('signupsuccess')
    else:
	return HttpResponseRedirect('home')
    #return HttpResponseRedirect('signupsuccess')
    

def create(request):
    context = {}
    return render(request, 'stories/createstory.html', context)

def submitLine(request, storyID):
    sentence = request.POST['sentence']
    s = Story.objects.filter(id = storyID)
    s1 = s[0]
    u = request.user
    Line(content = sentence, story = s1, user = u).save()
    s1.lineNum += 1
    s1.save()
    print s1.lineNum
    return HttpResponseRedirect('/story/' + str(storyID))

def storyline(request, storyID):
    stories = Story.objects.filter(id = storyID)
    s = stories[0]
    list1 = ['Story Not Found']
    context = {'Lines':list1}
    if stories != []:
	lines = Line.objects.filter(story = s)
	if s.lineNum == s.maxNum:
	    context = {'Lines':lines, 'storyTitle':s.title, 'storyID': str(s.id), 'bool' :True} 
    	else:
	    context={'Lines':[lines[len(lines)-1]], 'storyTitle':s.title, 'storyID': str(s.id), 'bool' :False}	
    return render(request,'stories/storyline.html',context)


#def clear(request):
  #  s = Story.objects.filter(title = "Sadek the Duck")
  #  Line.objects.filter(story = s[0]).delete()
  #  return HttpResponseRedirect('story')

def newStory(request):
    title1 = request.POST['Title']
    firstLine = request.POST['firstLine']
    numStory = request.POST['numLine']
    u = request.user
    new = Story(title = title1, user = u, maxNum = numStory, lineNum = 1)
    new.save()
    Line(content = firstLine, user = u, story = new).save()
    return HttpResponseRedirect('/story/' + str(new.id))

@login_required    
def profile(request):
    context = {'storiesList':Story.objects.all(), 'user' : request.user}
    return render(request, 'stories/profile.html', context)

def signup(request):
    return render(request, 'stories/signuppage.html', {})

def signupsuccess(request):
    return render(request, 'stories/signupsuccess.html',{})

def Continue(request):
    stories = []
    list1 = Story.objects.all()
    for story in list1:
	if story.maxNum != story.lineNum:
	    stories.append(story)
    context = {'stories':stories}
    return render(request, 'stories/continue.html', context)

def library(request):
    stories = []
    list1 = Story.objects.all()
    for story in list1:
	if story.maxNum == story.lineNum:
	    stories.append(story)
    context = {'stories':stories}
    return render(request, 'stories/library.html', context)

def logOut(request):
    logout(request)
    return HttpResponseRedirect('/home')

