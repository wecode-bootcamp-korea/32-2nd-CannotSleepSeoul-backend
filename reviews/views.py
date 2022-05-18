import json

from django.views import View
from django.http  import JsonResponse

from hotels.models  import Hotel
from reviews.models import Review


class ReviewView(View):
    def get(self, request, hotel_id):
        
        if not Hotel.objects.filter(id=hotel_id).exists():
            return JsonResponse({'message':'HOTEL_DOES_NOT_EXIST'}, status=404)

        review_list = [{
            "id"        : review.id,
            "name"      : review.user.name,
            "rating"    : review.rating,
            "content"   : review.description,
            "create_at" : review.created_at
            } for review in Review.objects.filter(hotel_id=hotel_id)
        ]

        return JsonResponse({'data':review_list}, status=200)
