from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('reservations/', views.reservations, name="reservations"),
    path('book', views.book, name='book'),
    path('book', views.BookView.as_view()),
    path('menu-item', views.menu, name="menu"),
    path('menu-item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings', views.bookings, name='bookings'),
    path('specials', views.specials, name='specials'),
    path('events', views.events, name='events'),
    path('chefs', views.chefs, name='chefs'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('api-token-auth/', obtain_auth_token),
    path('booking', views.BookingView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('user', views.UserView.as_view()),
]