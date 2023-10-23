from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Staff(models.Model):
    name = models.CharField(_("Name"), max_length=50 )
    title = models.CharField(_("Title"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    x_username = models.CharField(_("X Username"), max_length=50 , blank=True, null=True)
    facebook_username = models.CharField(_("FB Username"), max_length=254 , blank=True, null=True)
    image= models.ImageField(_("Staff Image"), upload_to='stuff/')
    
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    persons = models.IntegerField(_("Persons") , default=0)
    message = models.TextField(_("Message"))


    def __str__(self):
        return self.name





