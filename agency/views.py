from django.shortcuts import redirect, render
from django.http import HttpResponse
from agency.models import *

# Create your views here.
def home(request): 
        return render(request,"agency/index.html")

def bookings(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phoneno = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        services = request.POST['services']
        comment = request.POST['comment']


        booking = Bookings(name=name, email=email, phone_no=phoneno, postal_address=address, city=city, servicies=services, comments=comment)
        booking.save_bookings()

        return redirect('/contact')
    else:
        return redirect('/contact')        

def contact(request):
    return render(request,"agency/contact.html") 

def admin(request):
    return render(request,"agency/admin.html")