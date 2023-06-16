from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200, null=True, blank=False)
    isHoliday = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Post(models.Model):
    email = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)

class LikeDislike(models.Model):
    email = models.CharField(max_length = 200)
    postId = models.IntegerField()
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)