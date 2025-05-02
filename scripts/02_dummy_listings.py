from random import choice, randint
import csv, os
from decimal import Decimal

from apps.accounts.models import User
from apps.listings.models import Listing
from core.settings import BASE_DIR


def run():
	csv_file_location = (
		"/home/joncorv/Documents/Pycharm/Nobnb/scripts/dummy_listings.csv"
	)
	dummy_img_directory = "static/img/listings/dummy_images"

	def random_user():
		return choice(User.objects.all())

	# read the csv vile and
	with open(csv_file_location, "r") as file:
		reader = csv.DictReader(file)
		for row in reader:
			# Create the listing
			listing = Listing(
				short_name=row["short_name"],
				name=row["name"],
				description=row["description"],
				city=row["city"],
				state_or_province=row["state_or_province"],
				country=row["country"],
				latitude=Decimal(row["latitude"]),
				longitude=Decimal(row["longitude"]),
				what_book_movie_show=row["what_book_movie_show"],
				num_deaths=int(row["num_deaths"]),
				nightly_rate=Decimal(row["nightly_rate"]),
				creator=random_user(),
				average_rating=Decimal(row["average_rating"]),
				# Note: imageset field is missing as it requires an actual file upload
			)
			listing.save()
			print(f"Created listing: {listing.short_name}")

			# Create an image folder for current listing
			listing_folder = BASE_DIR / dummy_img_directory / listing.id
			os.makedirs(listing_folder)