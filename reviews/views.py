import json

from django.shortcuts import render

from json.decoder     import JSONDecodeError

from django.views     import View
from django.http      import JsonResponse

from hotels.models    import Hotel, HotelImage, Location, Room, RoomType
from reviews.models   import Review
from users.models     import User

from users.decorator  import log_in_decorator

class ReviewView(View):
    @log_in_decorator
    def post(self, request, hotel_id):
        try:
            data         = json.loads(request.body)
            user         = request.user
            rating       = data.get('rating', None)
            content      = data.get('content', None)

            if not Hotel.objects.filter(id=hotel_id).exists():
                return JsonResponse({'message': 'HOTEL_DOES_NOT_EXIST'}, status=404)
            
            Review.objects.create(
                rating   = rating,
                content  = content,
                user     = user,
                hotel_id = hotel_id
                )

            return JsonResponse({'message':'SUCCESS'}, status=201)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)

    def get(self, request, hotel_id):
        if not Hotel.objects.filter(id=hotel_id).exists():
            return JsonResponse({'message':'REVIEW_DOES_NOT_EXIST'}, status=404)

        review_list = [{
            "name"      : User.objects.get(id=review.user.id).name,
            "content"   : review.description,
            "create_at" : review.created_at
            } for review in Review.objects.filter(hotel_id=hotel_id)
        ]

        return JsonResponse({'data':review_list}, status=200)

    @log_in_decorator
    def delete(self, request, hotel_id, comment_id):
        user_id  = request.user.id
        hotel_id = hotel_id
        
        if not Review.objects.filter(id=comment_id, hotel_id=hotel_id, user_id=user_id).exists():
            return JsonResponse({'message':'COMMENT_DOES_NOT_EXIST'}, status=404)

        Review.objects.filter(id=comment_id, hotel_id=hotel_id, user_id=user_id).first().delete()
        return JsonResponse({'message': 'SUCCESS'}, status=204)