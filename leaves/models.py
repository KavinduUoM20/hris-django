from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Leave(models.Model):
    LEAVE_TYPES = [
        ('vacation', 'Vacation'),
        ('sick_leave', 'Sick Leave'),
        ('personal_leave', 'Personal Leave'),
    ]

