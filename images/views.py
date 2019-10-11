from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Category

# Create your views here.

def welcome(request):
        images = Image.get_all_images()
        categories = Category.objects.all()
        locations = Location.objects.all()
        return render(request, 'welcome.html', {"images":images,"categories":categories,"locations":locations})

def search_image(request):
        categories = Category.objects.all()
        if 'image' in request.GET and request.GET['image']:
                category_item = request.GET.get('image')
                searched_image = Image.search_by_category(category_item)
                message = f"{category_item}"

                return render(request, 'search.html', {"images":searched_image,"message":message, "categories":categories})

        else:
                message = "You have'nt search for any term"
        return render(request, 'search.html', {"message": message})

def category(request):
        categories = Image.get_all_images()
        return render(request,'category.html', {"categories":categories})

def image_location(request):
        locations = Location.get_image_by_location()
        return render(request,'location.html', {"locations":locations})

def single_image(request,image_id):
        try:
                image = Image.objects.get(id = int(image_id))
        except DoesNotExist:
                raise Http404()
        return render(request, 'images.html', {"image":image})