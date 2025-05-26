import csv, os, requests
from random import choice, randint
from decimal import Decimal

from apps.accounts.models import User
from apps.listings.models import Listing, ListingImage
from core.settings import BASE_DIR, MEDIA_ROOT


def run():
    csv_file_location = (
        "/Users/jonncorv/PycharmProjects/Nobnb/scripts/dummy_listings.csv"
    )

    def random_user():
        return choice(User.objects.all())

    # read the csv vile and
    with open(csv_file_location, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
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
                search_terms=row["image_search_terms"],
                # Note: imageset field is missing as it requires an actual file upload
            )
            listing.save()
            print(f"Created listing: {listing.short_name}")
