from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.db import models
from .models import Image,Location
# Create your views here.
def introduction(request):
    images =Image.objects.all()
    return render(request,'first.html', {"images":images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'album/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any Image"
        return render(request, 'album/search.html',{"message":message})

def get_location(request,location):
    location_results = Location.objects.all()
    location_result = Image.objects.filter(picha_location__place)
    return render(request,'first.html',{'images':location_result,'location_results':location_results})