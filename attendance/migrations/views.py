from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from .models import Attendance
import pytz

def index(request):
    return render(request, 'attendance/index.html')
def add_attendance(request):
    if request.method == 'POST':
        checkin_desc = request.POST.get('checkin_desc')

        # Get the current user and date
        user = request.user
        date_today = timezone.now().date()

        # Set the desired time zone for the check-in
        user_time_zone = 'Asia/Colombo'  # Replace with the desired time zone (e.g., Asia/Colombo for Sri Lanka)
        local_tz = pytz.timezone(user_time_zone)




