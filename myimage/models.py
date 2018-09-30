from django.db import models
from datetime import datetime as dt

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 150)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_path = models.ImageField(upload_to = 'images/') 
    location = models.ForeignKey('Location', null= True)
    category = models.ForeignKey('Category', null= True)


    def save_image(self):
        self.save()

    def __str__(self):
        return self.name
        

    class meta:
        ordering = ['name'] 



class Location(models.Model):
    '''
    Image location model
    '''
    PLACES = (   
        ('Nairobi','Nairobi'),
        ('Lagos','Lagos'),
        ('Moscow','Moscow'),
        ('St.peterburg','St.peterburg'),
        ('Abuja','Abuja'),
        ('Yola','Yola'),
        ('Mombasa','Mombasa'),
        ('Dushanbe','Dushanbe'),
        ('Dar es salaam', 'Dar es salaam')

        )           

    name = models.CharField(max_length = 100, choices = PLACES)



    def save_location(self):
        self.save()

    def __str__(self):
        return self.name
        



class Category(models.Model):
    name = models.CharField(max_length = 30)



    def save_category(self):
        self.save()

    def __str__(self):
        return self.name
        


