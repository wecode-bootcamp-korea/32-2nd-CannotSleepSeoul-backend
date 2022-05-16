from django.urls import path

from hotels.views import DetailView, ListView, MainView

urlpatterns = [
    path('/<int:hotel_id>', DetailView.as_view()),
    path('/list', ListView.as_view()),
    path('/main', MainView.as_view())
]
