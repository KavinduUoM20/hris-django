from django.db import models
import datetime

class EmployeeManager(models.Manager):
    def get_queryset(self):
        '''
        Employee.objects.all() -> returns only active employees ie.is_deleted = False
        '''
        return super().get_queryset().filter(is_deleted=False)
