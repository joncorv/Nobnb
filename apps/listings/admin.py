from django.contrib import admin

from apps.listings.models import Listing, Review, ListingImage

# Register your models here.
admin.site.register(Listing)
admin.site.register(Review)
admin.site.register(ListingImage)
