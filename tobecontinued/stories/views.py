# Create your views here.
from django.shortcuts import render
from stories.models import Line, Story
from django.http import HttpResponseRedirect

def homePage(request):
    context = {}
    return render(request, 'stories/HomePage.html', context)

#def logIn(request):
 #   User1 = request.POST['username']
  #  Pass = request.POST['password']
   # usersL = User.objects.all
    #for user in usersL:
	#if user.username == User1 and user.password == Pass:
	 #   HttpResponseRedirect('profile/' + user)

def createUser(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['Email']
    userName = request.POST['UserName']
    password = request.POST['Password']
    new = User(username = userName, email = email, password = password, first_name = firstname, last_name = lastname)
    new.save()
    return HttpResponseRedirect('signupsuccess')
    

def create(request):
    context = {}
    return render(request, 'stories/createstory.html', context)

def submitLine(request, storyID):
    sentence = request.POST['sentence']
    s = Story.objects.filter(id = storyID)
    s1 = s[0]
    Line(content = sentence, story = s1).save()
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
    new = Story(title = title1, maxNum = numStory, lineNum = 1)
    new.save()
    Line(content = firstLine, story = new).save()
    return HttpResponseRedirect('/story/' + str(new.id))
    
def profile(request):
    context = {'storiesList':Story.objects.all()}
    return render(request, 'stories/profile.html', context)

def signup(request):
    return render(request, 'stories/signuppage.html', {})
