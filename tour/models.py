from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Agents(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Tours(models.Model):
    title = models.TextField(max_length=250)
    description = models.TextField(max_length=500, default='')

    agent = models.ForeignKey(
        Agents, on_delete=models.PROTECT, related_name='agents')

    def __str__(self):
        return self.title

# Pending Models names = Booking, Tours_Review, Customers,  Tour_Categories


class Customer(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='customer')

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class BookingTour(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    booking_date = models.DateField()


class TourReview(models.Model):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review of '{self.tour.title}' by {self.customer.name} ({self.rating} stars"


class TourCategory(models.Model):
    name = models.CharField(max_length=100)
    tours = models.ManyToManyField(Tours)

    def __str__(self):
        return f"{self.name}"
