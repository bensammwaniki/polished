from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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
# upload images for the available workers
def upload(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        sname = request.POST['sname']
        tname = request.POST['tname']
        phone_no = request.POST['phone_no']
        id_no = request.POST['id_no']
        dobdate = request.POST['dobdate']
        home_town = request.POST['home_town']
        occupation = request.POST['occupation']
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        add_team = Team(fname=fname, sname=sname, tname=tname,phone_no=phone_no, id_no=id_no, dobdate=dobdate, home_town=home_town, occupation=occupation)
        add_team.save_team_member()
        return redirect('/administ')
    return render(request, 'index.html')



# renders contact page 
def contact(request):
    return render(request,"agency/contact.html") 

# retuns data to the admin page 

@login_required(login_url='/accounts/login/')
def admin(request):
    bookings = Bookings.objects.all().order_by('-date')
    
    return render(request,"agency/admin.html", {'bookings':bookings})