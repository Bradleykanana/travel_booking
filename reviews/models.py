from django.db import models
from django.contrib.auth.models import User
from bookings.models import Booking
from destinations.models import Destination

class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
	destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True, blank=True)
	rating = models.PositiveSmallIntegerField(default=5)
	comment = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.rating}★"
