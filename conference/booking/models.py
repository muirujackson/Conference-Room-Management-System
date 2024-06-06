from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    purpose = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.room.name} booked by {self.user.username} from {self.start_time} to {self.end_time}"
