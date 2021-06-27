from django.contrib.auth.models import User
from django.utils import timezone


from django.db import models





class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    upload = models.FileField(upload_to='files/')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='userPics')

    def __str__(self):
        return self.user.username
