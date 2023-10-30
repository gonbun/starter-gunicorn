from django.db import models

# Create your models here.
class CalendarSchedule(models.Model):
    contents = models.CharField(max_length=80)
    created_at = models.DateTimeField()