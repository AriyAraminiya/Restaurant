from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class FoodName(models.Model):
    FOOD_TYPE=[
        ("drinks","Drinks"),
        ("lunch","Lunch"),
        ("dinner","Dinner"),
    ]
    name = models.CharField( max_length=100)
    description = models.CharField(_("Description"), max_length=250)
    rate = models.IntegerField(_("Rate") , default=0 )
    price = models.IntegerField()
    time = models.IntegerField(_("Prepare Time"))
    pub_date= models.DateField(_("Date of Release"), auto_now=False, auto_now_add=True)
    photo = models.ImageField( upload_to='foods/')
    type_food = models.CharField(_("Type Of Food"), max_length=10 , choices=FOOD_TYPE , default='drinks')
    
    
    def __str__(self):
        return self.name

class ImageSlider(models.Model):
    title = models.CharField(_("Image Title"), max_length=50)
    image = models.ImageField(_("Image"), upload_to='slider/')

    def __str__(self):
        return self.title
    
    
class Gallery(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"))
    image = models.ImageField(_("Image"),upload_to='gallery/')

    

    def __str__(self):
        return self.title




