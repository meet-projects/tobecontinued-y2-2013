from django.db import models
from django.contrib.auth.models import User

class Line (models.Model):
        user = models.ForeignKey(User)
	content = models.CharField(max_length=200)
	story = models.ForeignKey('Story')
	
	def __unicode__(self):
		return self.content

class Story (models.Model):
        user = models.ForeignKey(User)
	title = models.CharField(max_length=30)
        maxNum = models.IntegerField()
        lineNum = models.IntegerField()

	def __unicode__(self):
		return self.title

