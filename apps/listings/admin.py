from django.contrib import admin

from apps.listings.models import Listing, Review

# Register your models here.
admin.site.register(Listing)
admin.site.register(Review)
