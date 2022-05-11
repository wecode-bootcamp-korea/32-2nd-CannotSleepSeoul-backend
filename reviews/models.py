from cores.models import Timestamp
from django.db    import models

class Review(Timestamp):
    description = models.CharField(max_length=1000)
    rating      = models.DecimalField(max_digits=3, decimal_places=1)
    deleted_at  = models.DateTimeField(null=True)
    users_id    = models.ForeignKey('User', on_delete=models.CASCADE)
    hotels_id   = models.ForeignKey('Hotel', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'

class ReviewImage(models.Model):
    image_url  = models.CharField(max_length=200)
    reviews_id = models.ForeignKey('Review', on_delete=models.CASCADE)

    class Meta:
        db_table = 'review_images'
