from django.urls import path
from users.views import KakaoSignIn

urlpatterns = [
    path('/kakaosignin', KakaoSignIn.as_view()),
]