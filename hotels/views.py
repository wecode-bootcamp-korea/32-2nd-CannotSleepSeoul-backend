import json

from django.shortcuts import render

from django.views     import View
from django.http      import JsonResponse

from hotels.models    import Hotel, HotelImage, Location, Room, RoomType

class DetailView(View):
    def get(self, request, hotel_id):
        try:
            hotels = Hotel.objects.filter(id=hotel_id)

            hotel_detail = [{
                'id'            : hotel.id,
                'name'          : hotel.name,
                'latitude'      : hotel.latitude,
                'longitude'     : hotel.longitude,
                'introduction'  : hotel.introduction,
                'using_time'    : hotel.using_time,
                'facilities'    : hotel.facilities,
                'service'       : hotel.service,
                'information'   : hotel.information,
                'refund_policy' : hotel.service,
                'city'          : hotel.location.city,
                'gu'            : hotel.location.gu,
                'ro'            : hotel.location.ro,
                'detail'        : hotel.location.detail,
                'image_url'     : hotel.hotelimage_set.filter(hotel_id=hotel.id)[0].image_url,
                'room'          : [{
                    'room_id'              : room.id,
                    'available_date_start' : room.available_date_start,
                    'available_date_end'   : room.available_date_end,
                    'type'                 : room.room_type.type,
                    'price'                : room.room_type.price,
                    'image_url'            : room.roomimage_set.filter(room_id=room.id)[0].image_url
                    } for room in hotel.room_set.all()]
            } for hotel in hotels]

        except Hotel.DoesNotExist:
            return JsonResponse({'message' : 'HOTEL_DOES_NOT_EXIST'}, status=404)
        return JsonResponse({'hotel_detail': hotel_detail}, status=200)