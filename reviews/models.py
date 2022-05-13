from cores.models import TimeStamp
from django.db    import models

class Review(TimeStamp):
    description = models.CharField(max_length=1000)
    rating      = models.DecimalField(max_digits=3, decimal_places=1,null=True)
    deleted_at  = models.DateTimeField(null=True)
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE)
    hotel       = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'

class ReviewImage(models.Model):
    image_url = models.CharField(max_length=200,null=True)
    review    = models.ForeignKey('reviews.Review', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'review_images'
