from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
   
    url(r'^$',views.index,name='indexPage'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name='pastNews'),
    # url(r'^article/(\d+)',views.article,name ='article'),
    url(r'^search/', views.search_results,name='search_results'), 
    url('locations/<loc>', views.get_image_by_location, name='myLocations'),
    url(r'categories/<cat>',views.get_image_by_category,name='myCategories'),
   
]

