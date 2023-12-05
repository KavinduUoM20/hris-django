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

    return render(request, 'attendance/add_attendance.html')

    def view_attendance(request):
        # Retrieve all attendance records
        attendances = Attendance.objects.all()
        return render(request, 'attendance/view_attendance.html', {'attendances': attendances})

    def my_attendance(request):
        # Your logic for viewing user-specific attendance goes here
        return render(request, 'attendance/my_attendance.html')

    def update_attendance(request):
        # Get today's attendance for the current user
        user = request.user
        today_attendance = Attendance.objects.filter(user=user, date_today=timezone.now().date()).first()

        if today_attendance is None:
            # Handle the case where there is no attendance record for today
            messages.warning(request, 'No attendance record found for today.')
            return redirect('view_attendance')

        if request.method == 'POST':
            checkout_desc = request.POST.get('checkout_desc')

            # Set the desired time zone for the checkout
            user_time_zone = 'Asia/Colombo'  # Replace with the desired time zone (e.g., Asia/Colombo for Sri Lanka)
            local_tz = pytz.timezone(user_time_zone)

            # Get the current time in the user's time zone
            now = timezone.now()
            checkout = now.astimezone(local_tz).time()
            # Update the Attendance object with checkout details
            today_attendance.checkout = checkout
            today_attendance.checkout_desc = checkout_desc
            today_attendance.save()















