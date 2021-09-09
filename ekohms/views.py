from django.shortcuts import get_object_or_404, render

from .models import *
from django.urls import reverse


# Create your views here.

room_types = RoomType.objects.all()
room=Room.objects.all()
room_status=RoomStatus.objects.all()
context = {'rooms': room_types,'room_status':room_status,'room_no':room}



def index(request):
    return render(request, 'ekohms/index.html', context)


def rooms(request):
    return render(request, 'ekohms/rooms.html', context)


def contact(request):
    return render(request, 'ekohms/contact.html')


def about(request):
    context = {'title': 'About',
               'info': 'A fairy tale where your wishes come true'}
    return render(request, 'ekohms/about.html', context)


def rooms_detailed_view(request, room_id):
    room_detail = get_object_or_404(RoomType, pk=room_id)
    return render(request, 'ekohms/rooms_views.html',{'room': room_detail,'rooms': room_types,'room_no':room})
   
def booking(request,room_id):
    room_detail = get_object_or_404(RoomType, pk=room_id)
    return render(request, 'ekohms/booking.html',{'room': room_detail,'rooms': room_types,'room_no':room})

def payment(request,room_id):
    room_detail = get_object_or_404(RoomType, pk=room_id)
    return render(request, 'ekohms/payment.html',{'room': room_detail,'rooms': room_types,'room_no':room})


