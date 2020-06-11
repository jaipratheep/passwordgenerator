from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request,'generator/homepage.html')

def genpassword(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRESTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+')
    yourpassword = ''
    for x in range(length):
        yourpassword += random.choice(characters)


    return render(request,'generator/generatedpassword.html', {'password':yourpassword})

def about(request):
    return render(request, 'generator/about.html')
