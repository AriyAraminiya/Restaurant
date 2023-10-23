from django.shortcuts import render , get_object_or_404
from .models import FoodName , ImageSlider , Gallery
from django.core.paginator import Paginator

# Create your views here.

def food_list(request):
    food_list = FoodName.objects.all()
    image_slider= ImageSlider.objects.all()
    gallery = Gallery.objects.all()
    context = {
        'foods':food_list,
        'images':image_slider,
        'gallery':gallery,
        
    }
    return render(request,'foods/list.html',context)


def food_detail(request , id):
    food = get_object_or_404(FoodName , id=id )
    return render(request , 'foods/detail.html',{'food':food})

def menu_page(request):
    menu_page = FoodName.objects.all()
    return render(request,'foods/menu.html',{'menu_page':menu_page})

def gallery_page(request):
    gallery = Gallery.objects.all()
    paginator = Paginator(gallery, 6) #show me 6 pic
    page_number = request.GET.get('page')
    gallery_page = paginator.get_page(page_number)
    return render(request,'foods/gallery.html',{'gallery':gallery_page})
