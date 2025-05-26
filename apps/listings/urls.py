from django.urls import path

from .views import ListingsView, ListingDetailView

urlpatterns = [
    path("", ListingsView.as_view()),
    # temporary path here for listing detail. In future it should use the pk int
    # path('<int:listing_id>', listing_detail_view, name='listing_detail')
    # path("listing/<int:listing.id>", listing_detail_view, name="listing_detail"),
    path("listing/<uuid:id>", ListingDetailView.as_view(), name="listing_detail"),
]
