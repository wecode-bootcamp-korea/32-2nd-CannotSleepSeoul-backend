from django.urls import path
from users.views import KakaoSignIn

urlpatterns = [
    path('/signin/kakao', KakaoSignIn.as_view()),
]
