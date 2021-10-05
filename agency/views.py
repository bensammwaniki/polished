from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"agency/index.html")

def contact(request):
    return render(request,"agency/contact.html") 

def admin(request):
    return render(request,"agency/admin.html")