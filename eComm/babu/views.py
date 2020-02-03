from django.shortcuts import render
from babu import urls
# Create your views here.
def test(request):
    return render(request,"first.html")