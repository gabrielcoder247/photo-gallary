from django.db import models

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 150)
    image_path = models.ImageField(upload_to = 'images/') 
    location = models.ForeignKey('Location', null= True)
    category = models.ForeignKey('Category', null= True)


class Location(models.Model):
    name = models.CharField(max_length = 30)



class Category(models.Model):
    name = models.CharField(max_length = 30)


