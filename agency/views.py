from django.shortcuts import redirect, render
from django.http import HttpResponse
from agency.models import *

# Create your views here.
 
# renders home page

def home(request): 
        return render(request,"agency/index.html")


#  submits form data for bookings
def bookings(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        services = request.POST['services']
        comment = request.POST['comment']

        booking = Bookings(name=name, email=email, phone_no=phone_no, postal_address=address, city=city, servicies=services, comments=comment)
        booking.save_bookings()

        return redirect('/')
    else:
        return redirect('/contact')      

# renders contact page 
def contact(request):
    return render(request,"agency/contact.html") 

# retuns data to the admin page 
def admin(request):
    bookings = Bookings.objects.all().order_by('-date')
    
    return render(request,"agency/admin.html", {'bookings':bookings})