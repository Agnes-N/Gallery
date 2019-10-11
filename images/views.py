from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Category

# Create your views here.

def welcome(request):
    images = Image.get_all_images()
    return render(request, 'welcome.html', {"images":images})

def search_image(request):

    if 'image' in request.GET and request.GET['image']:
        category_item = request.GET.get('image')
        searched_image = Image.search_by_category(category_item)
        message = f"{category_item}"

        return render(request, 'search.html', {"searched_image":searched_image,"message":message})

    else:
        message = "You have'nt search for any term"
        return render(request, 'search.html', {"message": message})
def category(request):
    categories = Image.get_all_images()
    return render(request,'welcome.html', {"categories":categories})

def single_image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
            raise Http404()
    return render(request, 'images.html', {"image":image})