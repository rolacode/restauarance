from rest_framework import serializers
from .models import Booking, Category, MenuItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'full_name', 'email', 'phone_num', 
                  'reservation_date', 'reservation_slot', 'people', 'comment']
                
 
class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title_name']


class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title_name', 'price','inventory',
                  'menu_item_description', 'category', 'category_id']