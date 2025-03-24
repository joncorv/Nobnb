from datetime import datetime
from random import choice, random

from apps.accounts.models import User
from apps.listings.models import Listing, Review


def create_dummy_reviews(num_reviews=10):
	def random_date(start, end):
		delta = end - start
		return start + (delta * random())

	for listing in Listing.objects.all():
		for i in range(num_reviews):
			i = Review(
				listing=listing,
				creator=choice(User.objects.all()),
				body="replace me with the random word generator",
				rating=random() * 5,
				date_visited=random_date(datetime.now(), datetime.now()),
				was_murdered=bool(random()),
				does_recommend=bool(random()),
				murders_witnessed=random() * 100
			)
			i.save()