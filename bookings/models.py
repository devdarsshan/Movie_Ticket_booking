from django.db import models
from datetime import date

# Create your models here.

class Moviesdata(models.Model):
    Movie_name = models.CharField(max_length=255)
    Theatre_name =models.CharField(max_length=255)
    Theatre_location = models.CharField(max_length=255)
    Release_date = models.DateField()

    def __str__(self):
        return self.Movie_name
    
class Customer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    password = models.TextField()

class Booking(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)  # If using Django's User model
    movie = models.ForeignKey(Moviesdata, on_delete=models.CASCADE)  # Assuming Moviesdata model
    showtime = models.IntegerField(choices=[(1, '10 AM'), (2, '2 PM'), (3, '6 PM'), (4, '10 PM')])
    booked_date = models.DateField(default=date(2001, 1, 1))
    booking_date = models.DateField(auto_now_add=True) 
    booked_seats = models.TextField()  # Store comma-separated booked seats (e.g., 'A1,B2,C3')

    def __str__(self):
        return f"{self.user.username} - {self.movie.Movie_name} - {self.showtime} - {self.booked_seats}"
    