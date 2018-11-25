from django.shortcuts import render
from .models import Image


global locations, categories
locations = ['Nairobi','Lagos','Moscow','St.peterburg','Abuja','Yola']
categories = ['comics','general','regular']

# Create your views here.

def index(request):

    '''
    view function that handle request and gets that data to be sent to the template
    '''
    images = Image.objects.all()

    return render(request, 'index.html', {"images":images, "locations":locations,"categories":categories})

def search_results(request): 
      
    if 'image' in request.GET and request.GET["image"]:
        search_term =request.GET.get("image")
        search_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "searched":search_images})

    else:

        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})    

def get_image_by_category(request,cat):

    images =Image.filter_by_category(cat)

    return render(request, 'category.html', {"images":images, "locations":locations, "categories":categories})  


def get_image_by_location(request,loc):

    places =Image.filter_by_location(loc)

    return render(request, 'location.html', {"places":places, "locations":locations, "categories":categories})     








