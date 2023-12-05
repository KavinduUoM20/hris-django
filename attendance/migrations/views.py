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

        # Get the current time in the user's time zone
        now = timezone.now()
        checkin = now.astimezone(local_tz).time()

        # Create and save the Attendance object
        Attendance.objects.create(
            user=user,
            date_today=date_today,
            checkin=checkin,
            checkin_desc=checkin_desc
        )

        messages.success(request, 'Attendance added successfully!')
        return redirect('add_attendance')  # Redirect to the view_attendance page or any other page








