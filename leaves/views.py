from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Leave
from django.contrib import messages
from hris.decorators import allowed_users

@login_required(login_url='/authentication/login')
@allowed_users(allowed_roles=['employee','admin'])
def index(request):
    return render(request,'leaves/index.html')


