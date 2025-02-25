from django.urls import path

from .views import listings_view, listing_detail_view

urlpatterns = [
    path("", listings_view, name='listings'),

    # temporary path here for listing detail. In future it should use the pk int
    # path('<int:listing_id>', listing_detail_view, name='listing_detail')
    path('listing_detail/', listing_detail_view, name='listing_detail')
]