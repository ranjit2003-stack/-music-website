from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from datetime import date, timedelta
import datetime
from User.models import *
from Admin.models import *

# Create your views here.
def  hlo(request):
    return HttpResponse('WElcome')


def index(request):
  
    
    uid = request.session['user_id']
    first_name = Register.objects.get(id = uid).firstname
    genres = Genre.objects.all()
    context = {
        'genres':genres,
        'firstname':first_name
    }
    return render(request,'index.html', context)


def home(request):
    uid = request.session['user_id']
    first_name = Register.objects.get(id = uid).firstname
    genres = Genre.objects.all()
    context = {
        'genres':genres, 
        'firstname':first_name,
    }
    return render(request,'home.html', context)
def albums(request):
    return render(request,'albums.html')
def login(request):  
    if request.method == "POST":
        email= request.POST['email']
        password=request.POST['password']  
        
        if Register.objects.filter(email=email, password=password).exists():
            data = Register.objects.filter(email=email, password=password).values('id').first()
            request.session['user_id'] = data['id']
            
            
            if Usersub.objects.filter(user_id=data['id'], is_active=True).exists():
                
                subscription_details = Usersub.objects.get(user_id=data['id'], is_active=True)
                
                if not subscription_details.end_date > datetime.datetime.now().date():
                    
                    Usersub.objects.filter(user_id=data['id'], is_active=True).update(is_active=False)
                    return redirect('subscription')
                else:
                    
                    return redirect('usermovie')
            return redirect('subscription')
        
             
    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')  # Use consistent names
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('password1')

        
        # Check if passwords match
        if password == confirmpassword:
            if not Register.objects.filter(email=email).exists():
                # Create new user
                Register.objects.create(
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    phone=phone,
                    password=password, 
                    confirmpassword=confirmpassword
                )
                return redirect('login')
            else:               
                return redirect('register')
        else:
            return redirect('register')

          # Redirect to login after successful registration

    return render(request, 'register.html')  # Ensure the form renders for GET requests
def Musics(request):
    data=Music.objects.all()
    context = {'data':data}
        
    
    return render(request,'Musics.html',context)

def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        subject=request.POST['message']
        email= request.POST['email']
        Complaint.objects.create(
            name=name,
            subject=subject,
            email=email,)
        
    return render(request,'contact.html')
def Events(request):
    return render(request,'Events.html')
def genre(request):   
    return render(request,'genre.html')
    
    
def view_genre_music(request, genre_id):
    filtered_music = Music.objects.filter(genre_id=genre_id)
    context = {
        'filtered_music':filtered_music
    }
    return render(request, "view_genre_based_music.html", context)
def logOut(request):
    del request.session['user_id']

    return redirect('login')
def lyrics(request,music_id):
    uid = request.session.get('user_id')
    songs = Music.objects.get(id = music_id)
    
    context = {
        'songs':songs,
        
    }
    return render( request,'lyrics.html',context)
def profile(request):
    if request.method == "POST":
        
        firstname= request.POST['firstname']
        lastname=request.POST['lastname']
        email= request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        
        uid = request.session.get('user_id')
        
        Register.objects.filter(id=uid).update(
           firstname=firstname,
           lastname=lastname,
           email=email,
           password= password,
           phone=phone,
           
    
    
           
        )
    return render(request,'home.html')

def viewprofile(request):
    uid = request.session['user_id']
    data =Register.objects.filter(id=uid)
    context= {'data':data}
    return render(request,"profile.html",context)

def subscription(request):
    data=Music.objects.all()
    context = {'data':data}
        
    
    
    return render(request,'subscription.html',context)
    

def payment(request):
    return render(request,'payment.html')
def comments(request,music_id):
    music = Music.objects.filter(id=music_id).first()  # Fetch movie or return None
    if not music:
        return redirect('userhome')  # Redirect if movie doesn't exist

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        user_id = request.session.get('user_id')  # Fetch user_id from session
         # Fetch user_name safely

        if comment_text and user_id:
            # Fetch the User instance correctly using the ID
            user = Register.objects.get(id=user_id) 
            if user:  # Ensure user exists in the database
                Comment.objects.create(
                    music=music,  # Associate the comment with the correct movie
                    user=user,  # Assign the correct User instance
                    comments=comment_text
                )

        # Ensure correct redirection based on URL pattern
        return redirect('musicdetail',music_id=music.id)

    # Show latest comments first
    data = Comment.objects.filter(music=music)
    
    return render(request, "musicdetail.html", {'music': music, 'data': data, 'music_id':music_id})

    

def musicdetail(request, music_id):
    music = get_object_or_404(Music, id=music_id)  # Fetch a single Music object
    
    
    context = {
        'music': music,  # Pass single object
        
    }
    return render(request, "musicdetail.html", context)
def like_music(request,music_id ):
    if 'user_id' not in request.session:
        return redirect('login')

    user = Register.objects.get(id=request.session['user_id'])
    music =Music.objects.get(id=music_id)

 
    existing_reaction = Like.objects.filter(user=user, music_id=music_id).first()

    if not existing_reaction:
        Like.objects.create(user=user, music=music, reaction="like")
        music.likes += 1
        music.save()

    return redirect('musicdetail', music_id=music.id)


def dislike(request,music_id):
    if 'user_id' not in request.session:
        return redirect('login')

    user = Register.objects.get(id=request.session['user_id'])
    music = Music.objects.get(id=music_id)

  
    existing_reaction = Like.objects.filter(user=user, music=music).first()

    if not existing_reaction:
        Like.objects.create(user=user, music=music, reaction="dislike")
        music.dislikes += 1
        music.save()

    return redirect('musicdetail', music_id=music.id)
   
def gpay(request):
    return render(request,"GPAY.HTML")
def credit(request):
    plans=Plan.objects.all()
    print(plans)
    return render(request,'creditpage.html',{"plans":plans})
def fav(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    user = Register.objects.get(id=request.session['user_id'])  # Assuming first user (Modify as per your auth setup)
    Favour.objects.create(user=user, music=music)
 

    return redirect('favourites')
def delete(request,music_id):
    Favour.objects.filter(id=music_id).delete()
    return redirect('favourites') 

def favourites(request):
    user = Register.objects.get(id=request.session['user_id'])   # Assuming first user (Modify as per your auth setup)
    favourites = Favour.objects.filter(user=user)
    return render(request, 'fav.html', {'favourites': favourites})

def subscribe(request):
    return redirect(subscribe)

def  home1(request):
    return render(request,'lyrics.html')