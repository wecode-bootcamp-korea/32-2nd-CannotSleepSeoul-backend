import json

from django.shortcuts import render

from json.decoder     import JSONDecodeError

from django.views     import View
from django.http      import JsonResponse

from hotels.models    import Hotel, HotelImage, Location, Room, RoomType
from reviews.models   import Review
from users.models     import User

class ReviewView(View):
    def get(self, request, hotel_id):
        if not Hotel.objects.filter(id=hotel_id).exists():
            return JsonResponse({'message':'REVIEW_DOES_NOT_EXIST'}, status=404)

        review_list = [{
            "name"      : User.objects.get(id=review.user.id).name,
            "rating"    : review.rating,
            "content"   : review.description,
            "create_at" : review.created_at
            } for review in Review.objects.filter(hotel_id=hotel_id)
        ]

        return JsonResponse({'data':review_list}, status=200)
