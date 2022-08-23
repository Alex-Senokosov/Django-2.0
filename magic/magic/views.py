from django.http import HttpResponse
from django.shortcuts import render
def about (request):
    a = 5+12
    return render(request,"about.html" , {"gritting": a})
def home (request):
    return HttpResponse("This is my home")