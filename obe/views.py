from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Booking, Menu, Contact
from datetime import datetime
import json
from .forms import BookingForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    return render(request, 'events.html')

def chefs(request):
    return render(request, 'chefs.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings":booking_json, 'date': date})
    

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        print("Form submitted!")
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)


# Add code for the bookings() view
def bookings(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = JsonResponse(list(bookings.values()), safe=False)
    return render(request, 'bookings.html', {'bookings': booking_json, 'date': date})
    

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

def specials(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'specials.html', {'specials': main_data})


@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).filter(email=data['email']).filter(
                people=data['people']).exists()

        if exist == False:
            booking = Booking(
                first_name=data['full_name'],
                email = data['email'],
                phone_num = data['phone_num'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
                people = data['people'],
                comment = data['comment'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')

    date = request.GET.get('date', datetime.today().date())
    
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')

def christmas(request):
    return render(request, 'christmas.html')