from django.urls import path

from hotels.views import ListView, MainView

urlpatterns = [
    path('/list', ListView.as_view()),
    path('/main', MainView.as_view())
]