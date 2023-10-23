from django.shortcuts import render
from .models import Staff 
from .forms import ContactForm

# Create your views here.

def staff_list(request):
    staff_list = Staff.objects.all()
    context = {
        'staff_list':staff_list
    }
    return render(request , 'contact/staff.html',context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = ContactForm()
            
    context = {
    'form':form ,
    }
    
    return render (request , 'contact/contact.html' , context)
            

