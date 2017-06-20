from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message

    def empty():
    	pass



    	
"""
class User(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message
"""