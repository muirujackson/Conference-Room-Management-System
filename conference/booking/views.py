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
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            purpose = form.cleaned_data['purpose']

            # Check for overlapping bookings
            if Booking.objects.filter(
                room=room,
                status='approved',
                start_time__lt=end_time,
                end_time__gt=start_time
            ).exists():
                messages.error(request, 'This room is already booked for the selected time period.')
            else:
                booking = Booking(
                    user=request.user,
                    room=room,
                    start_time=start_time,
                    end_time=end_time,
                    purpose=purpose,
                    status='pending'
                )
                booking.save()
                messages.success(request, 'Booking request created successfully. Waiting for approval.')
                return redirect('room_detail', room_id=room.id)
    else:
        form = BookingForm()
    return render(request, 'booking/create_booking.html', {'form': form, 'room': room})

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-start_time')
    return render(request, 'booking/user_bookings.html', {'bookings': bookings})