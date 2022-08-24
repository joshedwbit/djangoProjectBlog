from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    '''auto_now_add could be used in this field since this takes current datetime.  But we want this to be created not 
    last updated i.e. auto_now_add, however this isn't editable'''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    '''on delete means the post will get deleted if the user is deleted, but NOT vice versa'''
    
    def __str__(self):
        return self.title
        '''__ methods are called magic methods (OOP)'''
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})