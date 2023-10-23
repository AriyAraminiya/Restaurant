from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    description = models.CharField(_("Descriptin"), max_length=200)
    content = RichTextField(_("Content"))
    create_at = models.DateTimeField(_("Create at"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='blogs/',blank=True, null=True)
    category = models.ForeignKey("Category", verbose_name=_("Category"), related_name='blog' ,on_delete=models.CASCADE , blank=True, null=True)
    tags = models.ManyToManyField("Tags", related_name='blogs' ,verbose_name=_("Tags"))
    

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Blog_detail", kwargs={"pk": self.pk})
    
class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"))
    published_at = models.DateTimeField(_("Published at"), auto_now=False, auto_now_add=True)

    

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})

class Tags(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"))
    published_at = models.DateTimeField(_("Published at"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Tags_detail", kwargs={"pk": self.pk})

class Comments(models.Model):
    blog = models.ForeignKey("Blog", verbose_name=_("blog"), related_name="comments" , on_delete=models.CASCADE)
    name = models.CharField(_("Username"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    comment = models.TextField(_("Comment"))
    date = models.DateTimeField(_("Date"), auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Comments_detail", kwargs={"pk": self.pk})
    


