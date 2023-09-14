from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(reponse):
    return render(reponse, 'main/home.html')
