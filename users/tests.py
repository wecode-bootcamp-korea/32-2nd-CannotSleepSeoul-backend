import jwt

from django.test    import TestCase, Client
from django.conf    import settings

from unittest.mock  import patch
from users.models   import User
from django.conf    import settings
from CSS.settings   import SECRET_KEY, ALGORITHM
from datetime       import datetime, timedelta

class KakaoSignTest(TestCase):
    def setUp(self):
        User.objects.create(
            id       = 1,
            name     = "민석",
            kakao_id = 123456789,
            profile_image_url = "http://test.jpg"
        )

    def tearDown(self):
        User.objects.all().delete()

    @patch("users.views.requests.get")
    def test_kakao_signin_succes(self, mocked_kakao_user_info):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    "id": 123456789,
                    "properties": {
                        "nickname": "민석",
                        "profile_image": "http://test.jpg"
                    },
                    "kakao_account": {
                        "profile": {
                            "nickname": "민석"
                        }
                    }
                }

        mocked_kakao_user_info.return_value = MockedResponse()

        headers  = {"Authorization": "가짜 access_token"}
        response = client.post("/users/signin/kakao", **headers)

        access_token = jwt.encode({'id':1, 'exp':datetime.utcnow() + timedelta(days=1)}, SECRET_KEY, algorithm=ALGORITHM)
       
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'access_token' : access_token, "name" : "민석", "profile_image" : "http://test.jpg"})

    @patch("users.views.requests.get")
    def test_kakao_signup_success(self, mocked_kakao_user_info):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    "id": 1234567890,
                    "properties": {
                        "nickname": "성용",
                        "profile_image": "http://testing.jpg"
                    }
                }

        mocked_kakao_user_info.return_value = MockedResponse()

        headers  = {"Authorization": "가짜 access_token"}
        response = client.post("/users/signin/kakao", **headers)

        access_token = jwt.encode({'id':2, 'exp':datetime.utcnow() + timedelta(days=1)}, SECRET_KEY, algorithm=ALGORITHM)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'access_token' : access_token, "name" : "성용", "profile_image" : "http://testing.jpg"})