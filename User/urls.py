from django.urls import path
from User import views

urlpatterns = [
    path('hlo',views.hlo,name='hlo'),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('albums',views.albums,name='albums'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('Musics',views.Musics,name='Musics'),
    path('contact',views.contact,name='contact'),
    path('Events',views.Events,name='Events'),
    path('genre',views.genre,name='genre'),
    path('view_genre_music/<int:genre_id>',views.view_genre_music,name='view_genre_music'),
    path('logOut',views.logOut,name='logOut'),
    path('login', views.login, name='login'),
    path('lyrics/<int:id>',views.lyrics,name='lyrics'),
    path('profile',views.profile,name='profile'),
    path('viewprofile',views.viewprofile,name='viewprofile'),
    path('subscription',views.subscription,name='subscription'),
    path('payment',views.payment,name='payment'),
    path('comments/<int:music_id>/',views.comments, name='comments'),
    path('musicdetail/<int:music_id>/',views.musicdetail, name='musicdetail'),
    path('like_music/<int:music_id>/', views.like_music, name='like_music'),
    path('gpay',views.gpay,name='gpay'),
    path('credit',views.credit,name='credit'),
    path('favorites/<int:music_id>/',views.fav,name='fav'),
    path('dislike/<int:music_id>/',views.dislike,name='dislike'),
    path('delete/<int:music_id>/',views.delete,name='delete'),
    path('favourites',views.favourites,name='favourites'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('home1',views.home1,name='home1'),

    
    
    
   
    
]