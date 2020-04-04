from django.db import models
from django.utils import timezone



# User table
class Users(models.Model):
    u_id = models.CharField(max_length=30,primary_key=True)
    u_name = models.CharField(max_length=100)
    u_timezone = models.CharField(max_length=100)


class ActivityPeriods (models.Model):
    ap_id = models.AutoField(primary_key=True)
    ap_u_id = models.ForeignKey(Users, on_delete = models.CASCADE, blank=True, null=True, related_name='activity_periods')
    ap_starttime = models.DateTimeField(default=timezone.now, blank=True, null=True)
    ap_endtime = models.DateTimeField(default=timezone.now, blank=True, null=True)