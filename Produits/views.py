from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.
#Afficher les données à partir des fonctions

# def home(request):
    
#     #récuperations des données
#     donnees = Products.objects.all()
#     context = {
#         'donnees': donnees
#     }
#     return render(request, 'home.html', context)


#Afficher les données à partir de la classe vue générique

class Affichage(ListView):
    #Affichage du template
    template_name = 'home.html'
    #Récupération des données
    queryset = Products.objects.all()