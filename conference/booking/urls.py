from django.urls import path
from . import views

urlpatterns = [
    path('room/<int:room_id>/book/', views.create_booking, name='create_booking'),
]
