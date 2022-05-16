import csv
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CSS.settings')
django.setup()

from hotels.models import Hotel, Location, HotelImage, Room, RoomType, RoomImage
from reviews.models import Review

CSV_PATH = 'reviews.csv'
with open(CSV_PATH, newline='') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        Review.objects.create(
            id          = row[0],
            created_at  = row[1],
            updated_at  = row[2],
            description = row[3],
            rating      = row[4],
            deleted_at  = row[5],
            hotel_id    = row[6],
            user_id     = row[7]
        )

# CSV_PATH = 'locations.csv'
# with open(CSV_PATH, newline='') as in_file:
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
#         Location.objects.create(
#             id     = row[0],
#             city   = row[1],
#             gu     = row[2],
#             ro     = row[3],
#             detail = row[4]
#         )

# CSV_PATH = 'hotels.csv'
# with open(CSV_PATH, newline='') as in_file:
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
#         id            = row[0]
#         name          = row[1]
#         latitude      = row[2]
#         longitude     = row[3]
#         introduction  = row[4]
#         using_time    = row[5]
#         facilities    = row[6]
#         service       = row[7]
#         information   = row[8]
#         refund_policy = row[9]
#         location_id   = row[10]
#         Hotel.objects.create(
#             id = id,
#             name = name,
#             latitude = latitude,
#             longitude = longitude,
#             introduction = introduction,
#             using_time = using_time,
#             facilities = facilities,
#             service = service,
#             information = information,
#             refund_policy = refund_policy,
#             location_id = location_id
#         )

# CSV_PATH = 'hotel_images.csv'
# with open(CSV_PATH, newline='') as in_file:
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
#         id        = row[0]
#         image_url = row[1]
#         hotel_id  = row[2]
#         HotelImage.objects.create(
#             id        = id,
#             image_url = image_url,
#             hotel_id  = hotel_id
#         )

# CSV_PATH = 'room_types.csv'
# with open(CSV_PATH, newline='') as in_file:
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
#         id       = row[0]
#         type     = row[1]
#         price    = row[2]
  
#         RoomType.objects.create(
#             id       = id,
#             type     = type,
#             price    = price,
#         )

# CSV_PATH = 'rooms.csv'
# with open(CSV_PATH, newline='') as in_file:
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
#         id                   = row[0]
#         available_date_start = row[1]
#         available_date_end   = row[2]
#         hotel_id             = row[3]
#         room_type_id         = row[4]
#         Room.objects.create(
#             id                   = id,
#             available_date_start = available_date_start,
#             available_date_end   = available_date_end,
#             hotel_id             = hotel_id,
#             room_type_id         = room_type_id
#         )

# CSV_PATH = 'room_images.csv'
# with open(CSV_PATH, newline='') as in_file:
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
#         id        = row[0]
#         image_url = row[1]
#         room_id  = row[2]
#         RoomImage.objects.create(
#             id       = id,
#             image_url = image_url,
#             room_id = room_id
#         )