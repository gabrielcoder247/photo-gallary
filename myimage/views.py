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




