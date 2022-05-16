from django.urls import path

from reviews.views import ReviewView

urlpatterns = [
    path('/<int:hotel_id>', ReviewView.as_view())
]