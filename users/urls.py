from django.urls import path

from .views import Profile, Demandes

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('demande/', Demandes, name='demande'),
  

]
