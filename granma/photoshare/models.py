from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class GroupRoleUser(models.Model):
	ROLE_CHOICES = (
		('VWR', 'Viewer'),
		('ADM', 'Admin'),
		('MBR', 'Member')
	)
	role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='MBR')
	def __unicode__(self):
		return self.role

class Group(models.Model):
	name = models.CharField(max_length=35)
	gru = models.ForeignKey(GroupRoleUser)
	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	gru = models.ForeignKey(GroupRoleUser, null=True)
	email = models.EmailField()
	first_name = models.CharField(max_length=35)
	last_name = models.CharField(max_length=35)
	def __unicode__(self):
		return self.user.username

class Photo(models.Model):
	picfile = models.FileField(upload_to='photos/%Y/%m/%d')
	date_created = models.DateTimeField(default=datetime.now)
	creator = models.ForeignKey(UserProfile)
	def __unicode__(self):
		return (str(self.creator.user.username) + str(self.date_created))