import jwt
import requests

from django.views import View
from users.models import User
from django.http  import JsonResponse
from CSS.settings import SECRET_KEY, ALGORITHM
from datetime     import datetime, timedelta

class KakaoSignIn(View):
    def post(self, request):
        try:
            access_token       = request.headers.get('Authorization')
            kakao_info_api     = 'https://kapi.kakao.com/v2/user/me'
            headers            = {'Authorization':f'Bearer ${access_token}'}
            user_info_response = requests.get(kakao_info_api,headers=headers, timeout=5)
            user_info          = user_info_response.json()
            id                 = user_info['id']
            nickname           = user_info['properties']['nickname']
            profile_image      = user_info['properties']['profile_image']

            if not User.objects.filter(kakao_id=id).exists():
                User.objects.create(
                    kakao_id          = id,
                    name              = nickname,
                    profile_image_url = profile_image
                )

            access_token = jwt.encode({'id':id, 'exp':datetime.utcnow() + timedelta(days=1)}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({'access_token' : access_token})
        except KeyError:
            return JsonResponse({'message':'keyerror'},status=400)
        except requests.exceptions.Timeout:
            return JsonResponse({'message':'timeouterror'},status=408)
