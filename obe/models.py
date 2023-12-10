from django.db import models

# Create your models here.
class Booking(models.Model):
   full_name = models.CharField(max_length=255)
   email = models.EmailField()
   phone_num = models.CharField(max_length=100)
   reservation_date = models.DateField()
   reservation_slot = models.SmallIntegerField(default=10)
   people = models.SmallIntegerField(default=4)
   comment = models.TextField(max_length=1000, default='') 
   
   def __str__(self):
      return self.full_name


class Menu(models.Model):
   name = models.CharField(max_length=200, default='1') 
   price = models.FloatField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='')

   def __str__(self):
      return self.name
  
  
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200) 
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000, default='')
    
    def __str__(self):
       return self.full_name 
