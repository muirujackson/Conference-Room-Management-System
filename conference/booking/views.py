from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from rooms.models import Room
from .forms import BookingForm
from django.db.models import Q

@login_required
def create_booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room

            # Check for overlapping bookings
            if Booking.objects.filter(
                room=room,
                approved=True,
                start_time__lt=booking.end_time,
                end_time__gt=booking.start_time
            ).exists():
                messages.error(request, 'This room is already booked for the selected time period.')
            else:
                booking.save()
                messages.success(request, 'Booking request created successfully. Waiting for approval.')
                return redirect('room_detail', room_id=room.id)
    else:
        form = BookingForm()
    return render(request, 'booking/create_booking.html', {'form': form, 'room': room})
