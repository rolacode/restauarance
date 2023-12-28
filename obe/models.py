from django.db import models
from django.contrib.auth.models import User

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
   
class Category(models.Model):
      slug = models.SlugField()
      title_name = models.CharField(max_length=255, db_index=True)
      
      def __str__(self) -> str:
          return self.title_name

class MenuItem(models.Model):
   title_name = models.CharField(max_length=200, db_index=True) 
   price = models.FloatField(null=False) 
   inventory = models.SmallIntegerField()
   menu_item_description = models.TextField(max_length=1000, default='')
   category = models.ForeignKey(Category, on_delete=models.PROTECT)

   def __str__(self):
      return self.title_name
  
  
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200) 
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000, default='')
    
    def __str__(self):
       return self.full_name 
