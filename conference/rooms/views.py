from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Room
# from .models import Booking
# from .forms import BookingForm
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    bookings = {}
    return render(request, 'rooms/room_detail.html', {'room': room, 'bookings': bookings})

# @login_required
# def create_booking(request, room_id):
#     room = get_object_or_404(Room, id=room_id)
#     if request.method == 'POST':
#         # form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user = request.user
#             booking.room = room
#             booking.save()
#             messages.success(request, 'Booking created successfully.')
#             return redirect('room_detail', room_id=room.id)
#     else:
#         # form = BookingForm()
#     return render(request, 'booking/create_booking.html', {'form': form, 'room': room})

# def available_rooms(request, date):
#     date = parse_date(date)
#     rooms = Room.objects.all()
#     bookings = Booking.objects.filter(start_time__date=date)
#     booked_room_ids = bookings.values_list('room_id', flat=True)
#     available_rooms = rooms.exclude(id__in=booked_room_ids)
#     return render(request, 'rooms/available_rooms.html', {'available_rooms': available_rooms, 'date': date})

# def available_rooms_range(request, start_date, end_date):
#     start_date = parse_date(start_date)
#     end_date = parse_date(end_date)
#     rooms = Room.objects.all()
#     bookings = Booking.objects.filter(start_time__date__gte=start_date, start_time__date__lte=end_date)
#     booked_room_ids = bookings.values_list('room_id', flat=True)
#     available_rooms = rooms.exclude(id__in=booked_room_ids)
#     return render(request, 'rooms/available_rooms_range.html', {'available_rooms': available_rooms, 'start_date': start_date, 'end_date': end_date})
