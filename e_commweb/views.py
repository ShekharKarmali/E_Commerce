from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('<h1>This is my main page</h1>')
    return render(request,'shop/login.html')