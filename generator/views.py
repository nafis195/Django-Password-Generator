from operator import length_hint
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # function for home page rendering
    return render(request, 'generator/home.html')

def about(request):
    # function or about page rendering
    return render(request, 'generator/about.html')

def password(request):
    # function for password generator page rendering

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get("special"):
        characters.extend(list('!(@)#}${%^]&-[,_*;'))

    if request.GET.get("numbers"):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    thepassword = ""

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})