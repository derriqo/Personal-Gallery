from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image
# Create your views here.
def introduction(request):
    images =Image.get_image()
    return render(request,'first.html', {"images":images})

