from django.test import TestCase

# Create your tests here.
import jwt

from django.test         import TestCase, Client
from django.conf         import settings

from unittest.mock       import patch
from users.models        import User
from django.conf         import settings

class KakaoSignTest(TestCase):
    def setUp(self):
        User.objects.create(
            id       = 1,
            name     = "재관",
            kakao_id = 2237020088,
            email    = "cyc04088@naver.com"
        )
    
    def tearDown(self):
        User.objects.all().delete()
        
    @patch("users.views.requests.get")
    def test_kakao_signin_succes(self, mocked_kakao_user_info):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
    "id": 2237020088,
    "properties": {
        "nickname": "재관"
    },
    "kakao_account": {
        "profile": {
            "nickname": "재관",
            "profile_image_url": "http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg",
        },
        "has_email": True,
        "email": "cyc04088@naver.com",
        "gender": "male"
    }
}

        mocked_kakao_user_info.return_value = MockedResponse()

        headers  = {"Authorization": "가짜 access_token"}
        response = client.get("/users/kakao", **headers)
        
        user_id = jwt.decode(response.json()['new_token'], settings.SECRET_KEY, settings.ALGORITHM)
        new_token   = jwt.encode({'id':user_id['id']}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "REGISTERED_USER", "new_token" : new_token})
        
    @patch("users.views.requests.get")
    def test_kakao_signup_success(self, mocked_kakao_user_info):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
    "id": 123456789,
    "properties": {
        "nickname": "남규"
    },
    "kakao_account": {
        "profile": {
            "nickname": "남규",
            "profile_image_url": "http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg",
        },
        "gender": "male",
        "email" : "cyc04088@naver.com",
    }
}

        mocked_kakao_user_info.return_value = MockedResponse()

        headers  = {"Authorization": "가짜 access_token"}
        response = client.get("/users/kakao", **headers)
        
        user_id = jwt.decode(response.json()['new_token'], settings.SECRET_KEY, settings.ALGORITHM)
        new_token   = jwt.encode({'id':user_id['id']}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message" : "NEW_USER", "new_token" : new_token})