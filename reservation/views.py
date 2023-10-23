from django.shortcuts import render
from .forms import ReservationForm

# Create your views here.

def reservation(request):
    reserve = ReservationForm()
    if request.method == 'POST':
        reserve = ReservationForm(request.POST)
        if reserve.is_valid():
            reserve.save()
            
    else:
        reserve = ReservationForm()
    return render(request,'reservation/reservation.html',{'form':reserve})
