from random import choice, randint

from apps.accounts.models import User
from apps.listings.models import Listing


def create_dummy_listings():
	def rand_user():  # Returns a random user
		return choice(User.objects.all())

	def rand_deaths():  # Function that returns random int
		return randint(1, 100)

	# Create Dummy Users
	tomsmith = User()
	tomsmith.first_name = "tom"
	tomsmith.last_name = "smith"
	tomsmith.username = "tomsmith"
	tomsmith.save()

	# It Mansion
	pennywise_lair = Listing()
	pennywise_lair.name = "The Rustic Lair of Your Dreams"
	pennywise_lair.description = "insert dummy data"
	pennywise_lair.city = "Derry"
	pennywise_lair.state_or_province = "Maine"
	pennywise_lair.country = "USA"
	pennywise_lair.villain = "Pennywise"
	pennywise_lair.what_book_movie_show = "It"
	pennywise_lair.creator = rand_user()
	pennywise_lair.num_deaths = rand_deaths()
	pennywise_lair.save()

	# Dracula's Mansion
	draculas_mansion = Listing()
	draculas_mansion.name = "Draculas Mansion in the hills"
	draculas_mansion.description = "insert dummy data"
	draculas_mansion.city = "City"
	draculas_mansion.state_or_province = "Transylvania"
	draculas_mansion.country = "Transylvania"
	draculas_mansion.villain = "Dracula"
	draculas_mansion.what_book_movie_show = "Dracula's Revenge"
	draculas_mansion.creator = rand_user()
	draculas_mansion.num_deaths = rand_deaths()
	draculas_mansion.save()

	# Texas Chainsaw Massacre House
	texas_chains_massacre = Listing()
	texas_chains_massacre.name = "Quaint Murder House in Texas"
	texas_chains_massacre.description = "insert dummy data"
	texas_chains_massacre.city = "Blueville"
	texas_chains_massacre.state_or_province = "USA"
	texas_chains_massacre.country = "Texas"
	texas_chains_massacre.villain = "Leatherface"
	texas_chains_massacre.what_book_movie_show = "Texas Chainsaw Massacre"
	texas_chains_massacre.creator = rand_user()
	texas_chains_massacre.num_deaths = rand_deaths()
	texas_chains_massacre.save()