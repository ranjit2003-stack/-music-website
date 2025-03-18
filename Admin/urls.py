from django.urls import path
from Admin import views

urlpatterns = [
    path('adminhome',views.adminhome,name='adminhome'),
    path('addmusic',views.addmusic,name='addmusic'),
    path('viewmusic',views.viewmusic,name='viewmusic'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('editmusic/<int:id>',views.editmusic,name='editmusic'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('viewmore/<int:id>',views.viewmore,name='viewmore'),
    path('viewusers',views.viewusers,name='viewusers'),
    # #
    path('addgenre',views.addgenre,name='addgenre'),
    path('viewgenre',views.viewgenre,name='viewgenre'),
    path('viewgenmore/<int:id>',views.viewgenmore,name='viewgenmore'),
    path('editgenre/<int:id>',views.editgenre,name='editgenre'),
    path('edit1/<int:id>',views.edit1,name='edit1'),
    path('delete_1/<int:id>',views.delete_1,name='delete_1'),
    path('viewcomplaint',views.viewcomplaint,name='viewcomplaint'),
    path('viewcomment/<int:musicid>',views.viewcomment,name='viewcomment'),
    path('delete2/<int:id>',views.delete2,name='delete2'),
    path('viewlike/<int:music_id>',views.viewlike,name='viewlike'),
    path('plan',views.plan,name='plan')
 
   
    
]