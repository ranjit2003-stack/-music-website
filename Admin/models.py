from django.db import models


# Create your models here.
  
class Genre(models.Model):
    genre=models.CharField(max_length=50)
    image=models.ImageField(upload_to='profiles', default="Sample.jpg")

class  Music(models.Model):
    genre_id=models.ForeignKey(Genre, on_delete=models.CASCADE,null=True)
    musicname = models.CharField(max_length=100)
    artistname = models.CharField(max_length=100)
    musicdirector = models.CharField(max_length=100)
    musicproducer = models.CharField(max_length=100)
    date=models.DateField(null=True)
    songs=models.FileField(upload_to='albums', default="Sample.mp3")
    image=models.ImageField(upload_to='profiles', default="Sample.jpg")
    lyrics=models.CharField(max_length=200,null=True)
    likes = models.PositiveIntegerField(default=0)  # Store total likes
    dislikes = models.PositiveIntegerField(default=0) 

class  Plan(models.Model):
    plan_name = models.CharField(max_length=100)  # Example: Free, Premium, Family
    price=models.IntegerField(null=True)
    duration_days = models.IntegerField(null=True)
    
   
    



    