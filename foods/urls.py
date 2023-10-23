from django.urls import path
from . import views

app_name = 'foods'

urlpatterns = [
    path('',views.food_list,name='food_list'),
    path('<int:id>/',views.food_detail,name='food_detail'),
    path('menu/',views.menu_page,name='menu'),
    path('gallery/',views.gallery_page,name='gallery'),

    
]
