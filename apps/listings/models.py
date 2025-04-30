import uuid
from django.db import models

from apps.accounts.models import User


# Listings of famous horror movie properties. Real and imagined.
class Listing(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	# General Facts about the Listing
	short_name = models.CharField(max_length=50)  # Short name for search page
	name = models.CharField(max_length=100)  # Long name for detail page
	description = models.TextField()  # 100+ word description of the property.

	# Location information. Can be worldwide.
	city = models.CharField(max_length=100)
	state_or_province = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)

	# villain = models.CharField(max_length=100) # disabled for now
	what_book_movie_show = models.CharField(max_length=100)  # Source material
	num_deaths = models.IntegerField()  # How many people died here in book/movie
	nightly_rate = models.DecimalField(max_digits=7, decimal_places=2)  # rand cost

	# User and Creation Info
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# Profile images. Can we turn this into a TMDB or IMDB or Google scraper?
	imageset = models.ImageField(upload_to="listing_images")

	# Review Stats. This should be revised to be a calculated field.
	average_rating = models.DecimalField(max_digits=3, decimal_places=2)

	def __str__(self):
		return f"{self.short_name} from {self.what_book_movie_show} in {self.city}, {self.state_or_province}"


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