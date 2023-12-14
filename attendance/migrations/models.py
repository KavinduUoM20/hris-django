from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_today = models.DateField(auto_now_add=True)
    checkin = models.TimeField(null=True, blank=True)
    checkin_desc = models.TextField(blank=True)
    checkout = models.TimeField(null=True, blank=True)
    checkout_desc = models.TextField(blank=True)
    hours = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date_today}"
