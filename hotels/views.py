
import json

from django.shortcuts import render

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from hotels.models    import Hotel, HotelImage, Location, Room, RoomType

class MainView(View):
    def get(self, request):
        try:
            hotels = Hotel.objects.all()

            hotel_info = [{
                'id'        : hotel.id,
                'gu'        : hotel.location.gu,
                'image_url' : hotel.hotelimage_set.filter(hotel_id=hotel.id)[0].image_url,
                'name'      : hotel.name,
                'price'     : min([room.room_type.price for room in hotel.room_set.all()]),
                'rating'    : hotel.review_set.filter(hotel_id=hotel.id)[0].rating
            } for hotel in hotels]

            return JsonResponse({'hotel_info' : hotel_info}, status = 200)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)

class ListView(View):
    def get(self, request):
        try:
            hotel_name = request.GET.get('hotelName', None)
            searching  = request.GET.get('locationGu', None)
            page       = int(request.GET.get('page', 0))
            limit      = int(request.GET.get('limit', 30))
            offset     = (page*limit)
            check_in   = request.GET.get('check_in', None)
            check_out  = request.GET.get('check_out', None)
            reserved_rooms = []
            
            q = Q()

            if hotel_name:
                q &= Q(hotel_name=hotel_name)

            if searching:
                q &= Q(name_icontains=searching)

            hotels = Hotel.objects.filter(q).order_by('?')[offset:offset+limit]

            hotel_list = [{
                'hotel_id'  : hotel.id,
                'name'      : hotel.name,
                'image'     : hotel.hotelimage_set.filter(hotel_id=hotel.id)[0].image_url,
                'city'      : hotel.location.city,
                'gu'        : hotel.location.gu,
                'ro'        : hotel.location.ro,
                'detail'    : hotel.location.detail,
                'price'     : min([room.room_type.price for room in hotel.room_set.all()]),
                'latitude'  : hotel.latitude,
                'longitude' : hotel.longitude,
            } for hotel in hotels]

            return JsonResponse({'hotel_list' : hotel_list}, status = 200)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)