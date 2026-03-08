from django.urls import path
from .views import *

urlpatterns = [
    #path('', home, name='home'),
    path('',Affichage.as_view(),name='home')
]