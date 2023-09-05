from django.urls import path,register_converter
from . import views
from .converters import DateConverter

register_converter(DateConverter, 'date')

urlpatterns = [
    path('',views.signup,name='signup'),
    path('booking-history/<int:user_id>/',views.booking_history, name='booking_history'),
    path('movies-list/<int:user_id>/', views.movies_list, name='movies_list'),
    path('show-timings/<int:user_id>/<int:movie_id>/', views.show_timings, name='show_timings'),
    path('view_tickets/<int:user_id>/<int:movie_id>/<int:showtime>/<str:date_event>/', views.view_tickets, name='view_tickets'),

    # path('input',views.prediction,name="input")
]