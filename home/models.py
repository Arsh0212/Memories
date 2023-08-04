from django.db import models

# Create your models here.


class info(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=30, primary_key=True)
    password = models.IntegerField()
    img_id = models.CharField(max_length=100, blank=True)
    vid_id = models.CharField(max_length=100, blank=True)


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.ImageField(upload_to="images/", blank=True, null=True)


class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    vid = models.FileField(upload_to="videos/", blank=True, null=True)
