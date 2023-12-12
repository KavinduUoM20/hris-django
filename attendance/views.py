from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from .models import Attendance
from hris.decorators import allowed_users
import pytz


def index(request):
    return render(request, 'attendance/index.html')


@allowed_users(allowed_roles=['employee'])
def add_attendance(request):
    user = request.user
    date_today = timezone.now().date()

    # Check if the user has marked check-in for today
    has_checkin_today = Attendance.objects.filter(user=user, date_today=date_today, checkin__isnull=False).exists()
    is_completed = check_attendance(request)

    if request.method == 'POST':
        checkin_desc = request.POST.get('checkin_desc')

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

        messages.success(request, 'Check-in added successfully!')
        return redirect('add_attendance')  # Redirect to the view_attendance page or any other page

    return render(request, 'attendance/add_attendance.html', {'has_checkin_today': has_checkin_today, 'is_complete': is_completed})


@allowed_users(allowed_roles=['admin'])
def view_attendance(request):
    # Retrieve all attendance records
    attendances = Attendance.objects.all()
    return render(request, 'attendance/view_attendance.html', {'attendances': attendances})


# @login_required(login_url='/authentication/login')
# def my_attendance(request):
#     if request.method == 'GET':
#         user_attendance = Attendance.objects.filter(user=request.user)
#         return render(request, 'attendance/my_attendance.html', {'user_attendance': user_attendance})

def check_attendance(request):
    user_attendance_today = Attendance.objects.filter(
        user=request.user,
        date_today=timezone.now().date(),
        checkin__isnull=False,
        checkout__isnull=False
    ).exists()

    return True if user_attendance_today else False
@login_required(login_url='/authentication/login')
def my_attendance(request):

    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        user_attendance = Attendance.objects.filter(user=request.user)

        # Filter by start_date and end_date if provided
        if start_date and end_date:
            user_attendance = user_attendance.filter(date_today__range=[start_date, end_date])

        return render(request, 'attendance/my_attendance.html', {'user_attendance': user_attendance})

    return render(request, 'attendance/my_attendance.html')  # Handle other HTTP methods if needed


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

        checkin_datetime = datetime.combine(today_attendance.date_today, today_attendance.checkin)
        checkout_datetime = datetime.combine(today_attendance.date_today, checkout)
        hours_worked = (checkout_datetime - checkin_datetime).seconds / 3600  # Convert seconds to hours
        hours_worked = round(hours_worked, 2)

        # Update the Attendance object with checkout details
        today_attendance.checkout = checkout
        today_attendance.checkout_desc = checkout_desc
        today_attendance.hours = hours_worked
        today_attendance.save()

        request.session['checkout_form_submitted'] = True

        messages.success(request, 'Checkout details updated successfully!')
        return redirect('add_attendance')  # Redirect to the view_attendance page or any other page

    return render(request, 'attendance/add_attendance.html', {'attendance': today_attendance})
