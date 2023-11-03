from django.db import models
import uuid


# Create your models here.
class CalendarSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contents = models.CharField(max_length=80)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    zone = models.CharField(max_length=80)
    currency = models.CharField(max_length=5)
    importance = models.CharField(max_length=10)
    event = models.CharField(max_length=255)
    actual = models.CharField(max_length=30)
    forecast = models.CharField(max_length=30)
    previous = models.CharField(max_length=30)
    event_jp = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
