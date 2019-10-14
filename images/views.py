from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Category,Location
import pyperclip

# Create your views here.

def welcome(request):
        images = Image.get_all_images()
        return render(request, 'welcome.html', {"images":images})

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

def image_location(request,location_id):
        location_of_image = Image.filter_by_location(location_id)
        return render(request,'location.html', {"location_of_image":location_of_image})

def image(request,image_id):
        try:
                image = Image.objects.get(id = image_id)
        except DoesNotExist:
                raise Http404()
        return render(request, 'images.html', {"image":image})

def copy_image_url(request, image_id):
        images = Image.get_all_images()
        loc = Image.objects.get( id = image_id)
        pyperclip.copy('https://reinagallery1.herokuapp.com' + loc.pic_image.url)
        pyperclip.paste()
        return render(request, 'welcome.html', {"images":images})
