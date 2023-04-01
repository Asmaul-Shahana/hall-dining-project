from django.db import models

# Create your models here.

class Breakfast(models.Model):
    brfast_name = models.CharField(primary_key=True, max_length=100, unique=True)
    brfast_price = models.CharField(max_length=150)

class Lunch(models.Model):
    lunch_name = models.CharField(primary_key=True, max_length=100, unique=True)
    lunch_price = models.CharField(max_length=150)

class Snacks(models.Model):
    snacks_name = models.CharField(primary_key=True, max_length=100, unique=True)
    snacks_price = models.CharField(max_length=150)

class Dinner(models.Model):
    dinner_name = models.CharField(primary_key=True, max_length=100, unique=True)
    dinner_price = models.CharField(max_length=150)

class Events(models.Model):
    event_name = models.CharField(primary_key=True, max_length=100, unique=True)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_coupon_price = models.CharField(max_length=150)


class Booking(models.Model):
    st_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    meal = models.CharField(max_length=50)
    date = models.DateField()
    # time = models.TimeField()
    guests = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return self.name


