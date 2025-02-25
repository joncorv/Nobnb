from django.shortcuts import render

def listings_view(request):
    return render(request, 'listings.html')

def listing_detail_view(request):
    return render(request, 'listing_detail.html')
