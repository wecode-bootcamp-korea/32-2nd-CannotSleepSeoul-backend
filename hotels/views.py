import json

from datetime            import timedelta, datetime
from django.views        import View
from django.http         import JsonResponse
from django.db.models    import Q, Avg, Min

from hotels.models       import Hotel
from reservations.models import Reservation

class DetailView(View):
    def get(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(id=hotel_id)

            hotel_detail = {
                'id'            : hotel.id,
                'name'          : hotel.name,
                'latitude'      : hotel.latitude,
                'longitude'     : hotel.longitude,
                'introduction'  : hotel.introduction,
                'using_time'    : hotel.using_time,
                'facilities'    : hotel.facilities,
                'service'       : hotel.service,
                'information'   : hotel.information,
                'refund_policy' : hotel.refund_policy,
                'city'          : hotel.location.city,
                'gu'            : hotel.location.gu,
                'ro'            : hotel.location.ro,
                'detail'        : hotel.location.detail,
                'image_url'     : hotel.hotelimage_set.all()[0].image_url, 
                'room'          : [{
                    'room_id'              : room.id,
                    'available_date_start' : room.available_date_start,
                    'available_date_end'   : room.available_date_end,
                    'type'                 : room.room_type.type,
                    'price'                : room.room_type.price,
                    'image_url'            : room.roomimage_set.all()[0].image_url
                } for room in hotel.room_set.all()]
            }

        except Hotel.DoesNotExist:
            return JsonResponse({'message' : 'HOTEL_DOES_NOT_EXIST'}, status=404)
        return JsonResponse({'hotel_detail': hotel_detail}, status=200)

class MainView(View):
    def get(self, request):
        try:
            hotels = Hotel.objects\
                          .annotate(rating_avg=Avg('review__rating'))\
                          .annotate(min_price=Min('room__room_type__price'))\
                          .all()

            hotel_info = [{
                'id'        : hotel.id,
                'gu'        : hotel.location.gu,
                'image_url' : hotel.hotelimage_set.all()[0].image_url,
                'name'      : hotel.name,
                'price'     : hotel.min_price,
                'rating'    : hotel.rating_avg
            } for hotel in hotels]

            return JsonResponse({'hotel_info' : hotel_info}, status = 200)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)

class ListView(View):
    def get(self, request):
        try:
            searching  = request.GET.get('search', None)
            offset     = int(request.GET.get('offset', 0))
            limit      = int(request.GET.get('limit', 30))
            check_in   = request.GET.get('check_in', None)
            check_out  = request.GET.get('check_out', None)
            
            reserved_rooms = [] 

            if check_in and check_out:    
                check_in  = datetime.strptime(check_in, '%Y-%m-%d')
                check_out = datetime.strptime(check_out, '%Y-%m-%d')

                q_reservation = Q(check_out__range=[check_in + timedelta(days=1), check_out]) | \
                                Q(check_in__range=[check_in, check_out-timedelta(days=1)])

                reserved_rooms = Reservation.objects.filter(q_reservation)

            q = Q()

            if searching:
                q &= Q(location__gu__contains=searching)| Q(name__contains=searching)

            hotels = Hotel.objects\
                          .annotate(rating_avg=Avg('review__rating'))\
                          .annotate(min_price=Min('room__room_type__price'))\
                          .exclude(room__reservation__in=reserved_rooms)\
                          .filter(q).order_by('id')[offset:offset+limit]

            hotel_list = [{
                'hotel_id'  : hotel.id,
                'name'      : hotel.name,
                'image'     : hotel.hotelimage_set.all()[0].image_url,
                'city'      : hotel.location.city,
                'gu'        : hotel.location.gu,
                'ro'        : hotel.location.ro,
                'detail'    : hotel.location.detail,
                'price'     : hotel.min_price,
                'latitude'  : hotel.latitude,
                'longitude' : hotel.longitude,
            } for hotel in hotels]

            return JsonResponse({'hotel_list' : hotel_list}, status = 200)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status = 400)