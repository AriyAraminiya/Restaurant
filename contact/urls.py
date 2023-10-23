from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('staff/' , views.staff_list , name='staff'),
    path('' , views.contact , name='contact'),
]
