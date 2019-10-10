from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.

def welcome(request):
    images = Image.get_all_images()
    return render(request, 'welcome.html', {"images":images})

def search_image(request):

    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_image = Image.get_image_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"searched_image":searched_image,"message":message})