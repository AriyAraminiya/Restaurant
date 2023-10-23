from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(_("FullName"), max_length=200)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.CharField(_("Phonenumber"), max_length=50)
    numbers = models.IntegerField(_("Person"))
    date = models.DateField(_("Choose a day"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("Choose a Time"), auto_now=False, auto_now_add=False)
    


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
