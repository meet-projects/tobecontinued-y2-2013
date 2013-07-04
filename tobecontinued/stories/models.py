from django.db import models
from django.contrib.auth.models import User

class Line (models.Model):
        #user(who inputed the line, so they'll only see their own line)
	content = models.CharField(max_length=200)
	story = models.ForeignKey('Story')
	
	def __unicode__(self):
		return self.content

class Story (models.Model):
	title = models.CharField(max_length=30)
        maxNum = models.IntegerField()
        lineNum = models.IntegerField()

	def __unicode__(self):
		return self.title

