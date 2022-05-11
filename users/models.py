from django.db    import models
from cores.models import TimeStamp

class User(TimeStamp):
    kakao_id          = models.CharField(max_length=100)
    name              = models.CharField(max_length=10, null=True)
    email             = models.CharField(max_length=100, null=True)
    password          = models.CharField(max_length=50, null=True)
    profile_image_url = models.CharField(max_length=200, null=True)
    deleted_at        = models.DateTimeField(null=True)

    class Meta:
        db_table = 'users'