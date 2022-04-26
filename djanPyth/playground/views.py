from django.http import HttpResponse
from django.shortcuts import render
from requests import request

# Create your views here.
def say_hello(request):
    x=1
    y=2
    #return HttpResponse("hello world")
    return render(request,'first.html',{'name':'baba'})