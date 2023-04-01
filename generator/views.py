from django.shortcuts import render
from django.http import HttpResponse, request
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'asasasa'})

def password(request):
    # print(request.GET)
    chars = list("asdfghjklqwertyuiopmnbvcxz")
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
       chars.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get('special'):
       chars.extend(list('!@#$%^&*()'))
    if request.GET.get('number'):
       chars.extend(list('0123456789'))

    password = ''
    for char in range(length):
        password+=random.choice(chars)
    

    return render(request,'generator/password.html',{"password":password})

def about(request):
    return render(request,'generator/about.html')


def vazifa(request):
    str1 = str(request.GET.get('str1'))
    str2 = str(request.GET.get('str2'))
    print(type(str1))
    counts= str1.count(str2)
    # counts = str1.count(str2)   
    return render(request,'generator/vazifa.html', { "counts": counts})


