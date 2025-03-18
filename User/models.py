from django.db import models
from Admin.models import Music
from Admin.models import Plan
# Create your models here.
class  Register(models.Model):
    firstname=models.CharField(max_length=50,null=True)
    lastname=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)
    
    
class Complaint(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    subject=models.CharField( max_length=50)



class Usersub(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)   
    start_date = models.DateField(auto_now_add=True)  # When the subscription started
    end_date = models.DateField(null=True, blank=True)  # When it ends (if applicable)
    plan_id=models.ForeignKey(Plan,on_delete=models.CASCADE,null=True) 
    is_active = models.BooleanField(default=True)  # Check if the subscription is valid   
    
    
class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE,null=True)  
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)  
    comments = models.TextField()  # Allow longer comments
    firstname=models.CharField(max_length=50,null=True)
   
class Like(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=10)  
    
class Favour(models.Model):
    user=models.ForeignKey(Register, on_delete=models.CASCADE)
    music=models.ForeignKey(Music, on_delete=models.CASCADE)

   
   
    
    
    

    

