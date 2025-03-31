from django.urls import path
# from django.conf.urls import handler404
# from .views import custom_404_view

# handler404 = custom_404_view

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]