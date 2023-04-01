#from django.shortcuts import render
#from django.http import HttpResponse

#def index(response):
#def home(request):
   # return HttpResponse(request,"home.html")

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Breakfast

from .forms import CreateBookingForm

from .models import *
from .forms import CreateUserForm

def home(request):
    return render(request,"home.html")

#---------Register and login------------
def register (request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, "register.html", {'form':form})

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request,"about.html")
def notice(request):
    return render(request,"notice.html")
def help(request):
    return render(request,"help.html")
def events(request):
    eventobj = Events.objects.all()
    return render(request, "events.html", {'eventobj': eventobj} )
def breakfast(request):
    breakfastobj = Breakfast.objects.all()
    return render(request, "Breakfast.html", {'breakfastobj': breakfastobj} )
def lunch(request):
    lunchobj = Lunch.objects.all()
    return render(request, "Lunch.html", {'lunchobj': lunchobj} )
def snacks(request):
    snacksobj = Snacks.objects.all()
    return render(request,"Snacks.html", {'snacksobj': snacksobj} )
def dinner(request):
    dinnerobj = Dinner.objects.all()
    return render(request, "Dinner.html", {'dinnerobj':dinnerobj} )
# def book(request):
#     return render(request,"book.html")



def CreateBooking(request):
    if request.method == "POST":
        form = CreateBookingForm(request.POST)
        if form.is_valid():
            form.save()
            # form = CreateBookingForm()
            # return render(request, 'index.html', context)
            return redirect('booking-success')

    else:
        form = CreateBookingForm()

    bookings = Booking.objects.all()
    context = {'form': form, 'bookings': bookings}
    return render(request, 'book.html', context)

def booking_success_view(request):
    bookingobj = Booking.objects.last()
    return render(request, 'coupon.html', {'bookingobj':bookingobj} )


