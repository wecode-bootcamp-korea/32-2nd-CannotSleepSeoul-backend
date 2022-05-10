from django.db import models

class Hotel(models.Model):
    name      = models.CharField(max_length=100)
    latitude  = models.DecimalField(max_digits=8, decimal_places=3)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        db_table = 'hotels'

class Location(models.Model):
    city      = models.CharField(max_length=10)
    gu        = models.CharField(max_length=10)
    ro        = models.CharField(max_length=20)
    detail    = models.CharField(max_length=30)
    hotels_id = models.ForeignKey('Hotel', on_delete=models.CASCADE)

    class Meta:
        db_table = 'locations'

class HotelImage(models.Model):
    image_url = models.CharField(max_length=200)
    hotels_id = models.ForeignKey('Hotel', on_delete=models.CASCADE)

    class Meta:
        db_table = 'hotel_images'

class Room(models.Model):
    type                 = models.CharField(max_length=30)
    price                = models.DecimalField(max_digits=10, decimal_places=2)
    description          = models.CharField(max_length=10000)
    tag                  = models.CharField(max_length=50)
    available_date_start = models.DateField()
    available_date_end   = models.DateField()
    hotels_id            = models.ForeignKey('Hotel', on_delete=models.CASCADE)

    class Meta:
        db_table = 'rooms'

class RoomImage(models.Model):
    image_url = models.CharField(max_length=200)
    rooms_id  = models.ForeignKey('Room', on_delete=models.CASCADE)

    class Meta:
        db_table = 'room_images'