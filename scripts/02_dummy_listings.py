from random import choice, randint

from apps.accounts.models import User


def run():
    def rand_user():  # Returns a random user
        return choice(User.objects.all())

    def rand_deaths():  # Function that returns random int
        return randint(1, 100)
