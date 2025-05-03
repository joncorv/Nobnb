import csv, os, requests
from random import choice, randint
from decimal import Decimal

from apps.accounts.models import User
from apps.listings.models import Listing
from core.settings import BASE_DIR


def run():
    csv_file_location = (
        "/Users/jonncorv/PycharmProjects/Nobnb/scripts/dummy_listings.csv"
    )
    dummy_img_directory = "static/img/listings/dummy_images"

    def random_user():
        return choice(User.objects.all())

    # read the csv vile and
    with open(csv_file_location, "r", encoding="utf-8-sig") as file:
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
            listing_folder = f"{BASE_DIR}/{dummy_img_directory}/{listing.short_name}"
            os.makedirs(listing_folder)

            search_term = f"'{row["image_search_terms"]}'"
            count = 6

            # default data
            api_key = "rM5ZwdZtKEgHvY7f5ux0Z26RXcyZkkaGZoKDtC5hoGvxnBRxtFPO2tJ0"
            search_url = "https://api.pexels.com/v1/search"
            headers = {"Authorization": api_key}
            params = {"query": search_term, "per_page": count}

            # http request -> response
            response = requests.get(search_url, headers=headers, params=params).json()

            for i in range(count):
                image_save_path = f"{listing_folder}/{listing.short_name}_{i}.jpg"
                image_url = response.get("photos")[i].get("src").get("medium")
                image_response = requests.get(image_url)

                if image_response.status_code == 200:
                    with open(image_save_path, "wb") as file:
                        file.write(image_response.content)
                        print("Image downloaded successfully.")
                else:
                    print("Failed to download the image.")
