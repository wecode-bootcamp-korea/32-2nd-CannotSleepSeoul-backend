import uuid

from django.db    import models
from cores.models import TimeStamp

class Reservation(TimeStamp):
    reservation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    check_in         = models.DateField()
    check_out        = models.DateField()
    deleted_at       = models.DateTimeField(null=True)
    user             = models.ForeignKey('users.User', on_delete=models.CASCADE)
    room             = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservations'