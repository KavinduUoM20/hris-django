from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Leave(models.Model):
    LEAVE_TYPES = [
        ('vacation', 'Vacation'),
        ('sick_leave', 'Sick Leave'),
        ('personal_leave', 'Personal Leave'),
    ]

    LEAVE_STATUS = [
        ('requested', 'Requested'),
        ('rejected', 'Rejected'),
        ('approved', 'Approved'),
    ]
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_date = models.DateField(default=now)
    to_date = models.DateField()
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=LEAVE_STATUS, default='requested')

    def __str__(self):
        return f"{self.user.username} - {self.leave_type} Leave"
