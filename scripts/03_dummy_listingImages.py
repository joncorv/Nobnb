import csv, os, requests
from random import choice, randint
from decimal import Decimal

from apps.accounts.models import User
from apps.listings.models import Listing, ListingImage
from core.settings import BASE_DIR, MEDIA_ROOT


def run():
    dummy_img_directory = MEDIA_ROOT / "listing_images"
    # api setup
    api_key = "rM5ZwdZtKEgHvY7f5ux0Z26RXcyZkkaGZoKDtC5hoGvxnBRxtFPO2tJ0"
    search_url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": api_key}

    for listing in Listing.objects.all():

        # Create an image folder for current listing
        listing_folder_sm = f"{dummy_img_directory}/{listing.id}/sm"
        listing_folder_lg = f"{dummy_img_directory}/{listing.id}/lg"
        os.makedirs(listing_folder_sm, exist_ok=True)
        os.makedirs(listing_folder_lg, exist_ok=True)

        search_terms = listing.search_terms
        count = 6
        params = {"query": search_terms, "per_page": count}

        # http request -> response
        response = requests.get(search_url, headers=headers, params=params).json()

        for i in range(6):

            # instantiate an image object
            listing_image = ListingImage()
            listing_image.listing = listing

            # Download the small image
            image_save_path_sm = f"{listing_folder_sm}/{listing.id}_sm_{i}.jpg"
            image_url_sm = response.get("photos")[i].get("src").get("medium")
            image_response_sm = requests.get(image_url_sm)

            if image_response_sm.status_code == 200:
                with open(image_save_path_sm, "wb") as file:
                    file.write(image_response_sm.content)
                    print(
                        f"{listing.short_name} - Small Image #{i} downloaded successfully."
                    )
                    listing_image.image_sm = (
                        f"listing_images/{listing.id}/sm/{listing.id}_sm_{i}.jpg"
                    )

            else:
                print(f"{listing.short_name} - Small Image #{i} download failed.")

            # Download the Large image
            image_save_path_lg = f"{listing_folder_lg}/{listing.id}_lg_{i}.jpg"
            image_url_lg = response.get("photos")[i].get("src").get("large2x")
            image_response_lg = requests.get(image_url_lg)

            if image_response_lg.status_code == 200:
                with open(image_save_path_lg, "wb") as file:
                    file.write(image_response_lg.content)
                    print(
                        f"{listing.short_name} - Large Image #{i} downloaded successfully."
                    )
                    listing_image.image_lg = (
                        f"listing_images/{listing.id}/lg/{listing.id}_lg_{i}.jpg"
                    )

            else:
                print(f"{listing.short_name} - Large Image #{i} download failed.")

            listing_image.save()
