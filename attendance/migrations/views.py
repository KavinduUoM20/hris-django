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

