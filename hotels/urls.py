from django.urls import path

from hotels.views import DetailView

urlpatterns = [
    path('/<int:hotel_id>', DetailView.as_view())
]
