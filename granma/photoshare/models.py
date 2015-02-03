from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Group(models.Model):
    name = models.CharField(max_length=35)
    viewer = models.OneToOneField(User, null=True)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # gru = models.ForeignKey(GroupRoleUser, null=True, blank=True)
    email = models.EmailField()
    full_name = models.CharField(max_length=35)
    def __unicode__(self):
        return self.full_name

class GroupRoleUser(models.Model):
    ROLE_CHOICES = (
        ('VWR', 'Viewer'),
        ('ADM', 'Admin'),
        ('MBR', 'Member')
    )
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='MBR')
    group = models.ForeignKey(Group, null=True)
    user = models.ForeignKey(User, null=True)
    def __unicode__(self):
        return self.role

class Photo(models.Model):
    picfile = models.FileField(upload_to='photos/%Y/%m')
    date_created = models.DateTimeField(default=datetime.now)
    creator = models.ForeignKey(UserProfile, null=True)
    def __unicode__(self):
        return (str(self.creator.user.username) + str(self.date_created))

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)