from django.shortcuts import render

# Create your views here.
def listings_view(request):
    return render(request, 'listings.html')