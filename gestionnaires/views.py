from django.shortcuts import render
from rest_framework import views

# Create your views here.
def index(request):
    return render(request, 'gestionnaires/index.html' )

def facturation(request):
    return render(request, 'gestionnaires/facturation.html' )

def user(request):
    return render(request, 'gestionnaires/user.html' )

def plainte(request):
    return render(request, 'gestionnaires/plainte.html' )

def rapport(request):
    return render(request, 'gestionnaires/rapport.html' )

def reglage(request):
    return render(request, 'gestionnaires/reglage.html' )

def connect(request):
    return render(request, 'gestionnaires/connect.html' )

def inscrit(request):
    return render(request, 'gestionnaires/inscrit.html' )