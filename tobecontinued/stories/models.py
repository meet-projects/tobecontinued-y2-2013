from django.db import models

class Line (models.Model):
	content = models.CharField(max_length=200)
	story = models.ForeignKey('Story')
	
	def __unicode__(self):
		return self.content

class Story (models.Model):
	title = models.CharField(max_length=30)

	def __unicode__(self):
		return self.title
	
	
