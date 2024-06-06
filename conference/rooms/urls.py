from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    # path('room/<int:room_id>/book/', views.create_booking, name='create_booking'),
    # path('available_rooms/<str:date>/', views.available_rooms, name='available_rooms'),
    # path('available_rooms_range/<str:start_date>/<str:end_date>/', views.available_rooms_range, name='available_rooms_range'),
]