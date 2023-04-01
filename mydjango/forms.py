from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Booking


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']



MEALS = [
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('snack', 'Snack'),
    ('dinner', 'Dinner'),
    ('feast', 'Feast'),
    ]

NUMBER_OF_GUESTS= [tuple([x,x]) for x in range(1,6)]

GATEWAYS = [
    ('bkash', 'Bkash'),
    ('nagad', 'Nagad'),
    ('rocket', 'Rocket'),
    ('manual', 'Manual'),
    ]

class CreateBookingForm(forms.ModelForm):
    st_id = forms.CharField(label='Student ID',
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    meal = forms.CharField(label='Choose meal to book:', widget=forms.Select(choices=MEALS, attrs={'class': 'form-control'}))
    # meal = forms.CharField(
    #     max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control','type':'date'}))
    # time = forms.TimeField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}))
    guests = forms.IntegerField(label='Number of guests:',
        widget=forms.Select(choices=NUMBER_OF_GUESTS, attrs={'class': 'form-control'}))
    amount = forms.DecimalField(label='Payment Amount',
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    payment_method = forms.CharField(label='Payment Method:', widget=forms.Select(choices=GATEWAYS, attrs={'class': 'form-control'}))
    class Meta:
        model = Booking
        fields = ('st_id','name', 'email', 'meal', 'date', 'guests', 'amount', 'payment_method')
        # fields = ('emp_id', 'emp_name', 'dept')