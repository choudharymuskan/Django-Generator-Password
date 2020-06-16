from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request,'generate/home.html')
def about(request):
    return render(request,'generate/about.html')

def password(request):
    thepassword=''
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    for _ in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generate/password.html',{'password':thepassword})
# Create your views here.
