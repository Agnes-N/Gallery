from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.

def welcome(request):
    # images = Image.get_all_images()
    categories = Location.objects.all()
    return render(request, 'welcome.html', {"images":images, "categories":categories})

def search_image(request):

    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_image = Image.get_image_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"searched_image":searched_image,"message":message})

def category(request):
    categories = Image.get_all_images()
    return render(request,'category.html', {"categories":categories})

def single_image(request,image_id):
    image = Image.objects.get(id = image_id)
    return render(request, 'image.html', {"image":image})