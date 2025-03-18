from django.shortcuts import render,redirect
from django.http import HttpResponse
from Admin.models import *
from User.models import *


# Create your views here.

def adminhome(request):
    return render(request,'adminhome.html')  
def addmusic(request):
    genres=Genre.objects.all()
    context={'genres':genres}
    if request.method == "POST":
        genre=request.POST['genre']
        musicname= request.POST['name']
        artistname = request.POST['Name1']
        musicdirector = request.POST['Name2']
        musicproducer= request.POST['Name3']
        date = request.POST['date']
        songs = request.FILES['songs']
        Image=request.FILES['image']
        
        Music.objects.create(
            
            genre_id=Genre.objects.get(id=genre),
            musicname=musicname,
            artistname=artistname,
            musicdirector=musicdirector,
            musicproducer=musicproducer,
            date= date,
            songs=songs,
            image=Image,
           
        )
    
    return render(request,'addmusic.html',context)  
def viewmusic(request):
    data=Music.objects.all()
    context = {'data':data}
    return render(request,'viewmusic.html',context)  
def delete(request,id):
    data= Music.objects.filter(id=id).delete()
    return redirect('viewmusic')
def editmusic(request,id):
    data = Music.objects.filter(id=id)
    context = {
        'data':data,
    }
    return render(request, "editmusic.html", context)
def edit(request,id):
    if request.method == "POST":
        musicname= request.POST['name']
        artistname = request.POST['Name1']
        musicdirector = request.POST['Name2']
        musicproducer= request.POST['Name3']
        date = request.POST['date']
        songs = request.FILES['songs']
        image= request.FILES['image']
        
        Music.objects.filter(id=id).update(
            musicname=musicname,
            artistname=artistname,
            musicdirector=musicdirector,
            musicproducer=musicproducer,
            date= date,
            songs=songs,
            image=image,
           
        )
        return redirect('viewmusic')
    return render(request,'editmusic.html')
def viewmore(request,id):
    data=Music.objects.filter(id=id)
    context = {'data':data}
    return render(request,'viewmore.html',context)  
def viewusers(request):
    data=Register.objects.all()
    context ={'data':data}
    return render(request,'viewusers.html',context)
#######
def addgenre(request):
   
    if request.method == "POST":
        genre= request.POST['name']
        image = request.FILES['img']
        
        Genre.objects.create(
           genre=genre,
           image=image,
           
        )
    return render(request,'addgenre.html')
def viewgenre(request):
    data=Genre.objects.all()
    context = {'data':data}
    return render(request,'viewgenre.html',context)
def viewgenmore(request,id):
    data=Genre.objects.filter(id=id)
    context = {'data':data}
    return render(request,'viewgenmore.html',context)  
def editgenre(request,id):
    data = Genre.objects.filter(id=id)
    context = {
        'data':data,
    }
    return render(request, "editgenre.html", context)
def edit1(request,id):
    if request.method == "POST":
        genre= request.POST['name']
        image = request.FILES['img']
        
        Genre.objects.filter(id=id).update(
           genre=genre,
           image=image,
           
        )
        return redirect('viewgenre')
    return render(request,'editgenre.html')
def delete_1(request,id):
    Genre.objects.filter(id=id).delete()
    return redirect('viewgenre')
def viewcomplaint(request):
    data=Complaint.objects.all()
    context ={'data':data}
    
    return render(request,'viewcomplaint.html',context)

def viewcomment(request,musicid):
    
    comments = Comment.objects.filter(music=musicid).select_related('user')  # Get related comments with user data

    context = {
        'comments': comments,  # Pass comments to the template
    }
    
    return render(request, 'viewcomment.html', context)
def delete2(request,id):
    Comment.objects.filter(id=id).delete()
    return redirect('viewcomment') 
def viewlike(request, music_id):
    music = Music.objects.get(id=music_id)
    
    # Fix filtering: use 'reaction' instead of 'type'
    likes_count = Like.objects.filter(music=music, reaction='like').count()
    dislikes_count = Like.objects.filter(music=music, reaction='dislike').count()
    
    reactions = Like.objects.filter(music=music)

    return render(request, 'viewlike.html', {
        'music': music,
        'reactions': reactions,
        'likes_count': likes_count,
        'dislikes_count': dislikes_count
    })

def  plan(request):
    if request.method == "POST":
        plan=request.POST['name']
        price= request.POST['price']
        days = request.POST['days']
      
      
        
        Plan.objects.create(
            
            plan_name=plan,
            price=price,
            duration_days=days,)
           
    return render(request,'addplan.html')

    
    

  
    

    



    


