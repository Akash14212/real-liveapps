from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here. 
 
def home(request): 
    return HttpResponse("hello user.I am the HOME") 
 
def about(request): 
    return HttpResponse("This is a project about django")
 
def courses(request): 
    return HttpResponse("courses\n1.DataSceince \n2.AI") 
 
def edunet(request): 
    return render(request,'edunet.html')