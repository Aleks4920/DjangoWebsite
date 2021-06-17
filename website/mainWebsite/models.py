from django.contrib.auth.models import User
from django.utils import timezone


from django.db import models





class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    lastEdit = models.DateTimeField(auto_now=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='files/', null=True)
    postID = models.IntegerField(null=True)
    picture = models.ImageField(upload_to='images', null=True)



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
