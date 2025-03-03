from django.db import models
from apps.accounts.models import User

# Create your models here.
class Listing(models.Model):
	# General Facts about the Listing
	name = models.CharField(max_length=100)
	description = models.TextField()
	city = models.CharField(max_length=100)
	state_or_province = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	villain = models.CharField(max_length=100)
	what_book_movie_show = models.CharField(max_length=100)
	num_deaths = models.IntegerField()
	# User and Creation Info
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} from {self.what_book_movie_show} in {self.city}, {self.state_or_province}"

class Review(models.Model):
	# Each review points to a single Listing
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
	# User info
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# Review data
	body = models.TextField()
	rating = models.IntegerField()
	date_visited = models.DateTimeField()
	was_murdered = models.BooleanField()
	murders_witnessed = models.IntegerField()
	does_recommend = models.BooleanField()
