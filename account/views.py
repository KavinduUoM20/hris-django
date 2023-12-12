from django.shortcuts import render, redirect
from hris.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Account
from django.contrib import messages
from django.http import HttpResponse


def dashboard(request):
    return render(request, 'profile/dashboard.html')


def view_account(request):
    return render(request, 'profile/my_profile.html')


def add_profile(request):
    if request.method == 'GET':
        return render(request, 'profile/add_profile.html')
    if request.method == 'POST':
        # Extract user information
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        # Create a new User
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)

        # Assign the default group ('employee') to the user
        group = Group.objects.get(name='employee')
        user.groups.add(group)

        # Extract account information
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')

        # Create a new Account associated with the User
        account = Account.objects.create(
            user=user,
            address=address,
            email=email,
            phone=phone,
            profile_image=profile_image
        )

        # Add a success message
        messages.success(request, 'Account successfully created.')

        # Redirect to the dashboard or another appropriate page
        return redirect('dashboard')

    return HttpResponse("Method Not Allowed", status=405)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Get the form data
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Retrieve the current user's Account instance
        account_instance = request.user.account

        # Update the fields with the new data
        account_instance.user.username = username
        account_instance.user.first_name = first_name
        account_instance.user.last_name = last_name
        account_instance.phone = phone
        account_instance.email = email

        # Save the changes
        account_instance.user.save()
        account_instance.save()

        # Optionally, you can add a success message
        messages.success(request, 'Profile updated successfully.')

        # Redirect to a relevant page after the update
        return redirect('edit_profile')

    return render(request, 'profile/edit_profile.html')
