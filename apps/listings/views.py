from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, TemplateView, DetailView

from .models import Listing, ListingImage, Review
from apps.accounts.models import User


class ListingsView(ListView):
    template_name = "listings.html"
    # model = Listing
    queryset = Listing.objects.select_related("creator").prefetch_related(
        "listing_images"
    )


class ListingDetailView(DetailView):
    template_name = "listing_detail.html"
    model = Listing
    slug_field = "id"
    slug_url_kwarg = "slug"
    queryset = Listing.objects.select_related("creator").prefetch_related(
        "listing_images"
    )

    def get_object(self, queryset=None):
        """Override the get_object method"""
        queryset = self.get_queryset()
        try:
            # Fetch `id` from the URL kwargs
            obj = queryset.get(id=self.kwargs.get("id"))
            return obj
        except Listing.DoesNotExist:
            raise Http404("Listing not found")
