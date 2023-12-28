from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .forms import BookingForm
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Booking, MenuItem, Contact, Category, User
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer, CategorySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from datetime import datetime
import json


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "POST":
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes]
    
class BookView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "POST":
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes]    
    
class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        users = User.objects.filter(groups__name='Manager')
        return users  
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]    
    

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "POST":
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes] 
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory', 'category']
    search_fields = ['title_name']

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "POST":
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes] 
     
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return [(IsAuthenticated() or IsAdminUser())]
        return [permission() for permission in self.permission_classes]            

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
    menu_data = MenuItem.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = MenuItem.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

def specials(request):
    menu_data = MenuItem.objects.all()
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
                comment = data['msg'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')

    date = request.GET.get('date', datetime.today().date())
    
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')
