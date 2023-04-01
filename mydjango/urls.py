from django.urls import path
from .views import CreateBooking, booking_success_view
from . import views

urlpatterns =[
    path("",views.home, name="home"),
    path("about/",views.about, name="about"),
    path("notice/",views.notice, name="notice"),
    path("events/",views.events, name="events"),
    path("help/",views.help, name="help"),
    path("Breakfast/",views.breakfast, name="breakfast"),
    path("Lunch/",views.lunch, name="lunch"),
    path("Snacks/",views.snacks, name="snacks"),
    path("Dinner/",views.dinner, name="dinner"),
    path("register/",views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    # path("book/", views.book, name="book"),
    path('book/', CreateBooking, name='book'),
    path('book/coupon/', booking_success_view, name='booking-success'),
    #path('start/', views.index, name="index"),
]

#start
