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

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, update):
        updated =cls.objects.filter(id=id).update(image = update)

        return updated
        

    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.all(id = id).all()
        return images
                
    @classmethod
    def search_image(cls, category):

        searches = cls.objects.all(Category__name__icontain = category).all()
        return searches

    @classmethod
    def filter_by_location(self):
        locations = cls.objects.filter(Location__name__icontain = location).all()

        return locations          

    def __str__(self):
        return self.name
        

    class meta:
        ordering = ['-pub_date'] 



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
       

        )           

    location = models.CharField(max_length = 100, choices = PLACES)



    def save_location(self):
        self.save()



    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, update):
        updated =cls.objects.filter(id=id).update(location = update)

        return updated    

    def __str__(self):
        return self.name
        



class Category(models.Model):

    '''
    Image categories model
    '''

    CATEGORIES = (   
        ('comics','comics'),
        ('general','general'),
        ('regular','regular')
        )
       

    name = models.CharField(max_length = 30, choices= CATEGORIES)



    def save_category(self):
        self.save()


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, update):
        updated =cls.objects.filter(id=id).update(category = update)

        return updated    

    def __str__(self):
        return self.name
        


