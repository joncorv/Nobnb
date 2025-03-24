from scripts.dummy_listings import create_dummy_listings
from scripts.dummy_reviews import create_dummy_reviews
from scripts.dummy_users import create_dummy_users


def run():
	create_dummy_users()
	create_dummy_listings()
	create_dummy_reviews()