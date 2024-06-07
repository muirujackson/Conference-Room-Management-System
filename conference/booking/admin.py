from django.contrib import admin
from .models import Booking

# Register your models here.
class bookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_time', 'end_time','purpose','status')
    search_fields = ('user',)

admin.site.register(Booking, bookingAdmin) 