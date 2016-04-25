from __future__ import unicode_literals

from django.db import models



# Create your models here.

class BookCategory(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	active = models.BooleanField(default=None)

class Book(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(BookCategory)
	author = models.CharField(max_length=200)
	remark = models.TextField(blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=None)

	def __unicode__(self):
		return '(%s)' % (self.name)
