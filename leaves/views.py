from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Leave
from django.contrib import messages
from hris.decorators import allowed_users

@login_required(login_url='/authentication/login')
@allowed_users(allowed_roles=['employee','admin'])
def index(request):
    return render(request,'leaves/index.html')

@allowed_users(allowed_roles=['employee'])
def add_leaves(request):
    if request.method == 'GET':
        return render(request,'leaves/add_leaves.html')

    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        leave_type = request.POST.get('leave_type')
        description = request.POST.get('reason')  # 'reason' is the name attribute in your textarea

        if not from_date or not to_date or not leave_type or not description:
            messages.error(request, 'Please fill in all the fields.')
            return render(request, 'leaves/add_leaves.html')

        new_leave = Leave(
            user=request.user,
            from_date=from_date,
            to_date=to_date,
            leave_type=leave_type,
            description=description,
        )
        new_leave.save()

        messages.success(request, 'Applied Leave Successfully!')
        return render(request, 'leaves/add_leaves.html')

@allowed_users(allowed_roles=['admin'])
def view_leaves(request):
    if request.method == 'GET':
        leaves = Leave.objects.all()
        return render(request, 'leaves/view_leaves.html', {'leaves': leaves})

def update_leave(request, leave_id):
    if request.method == 'POST':
        # Retrieve the Leave object based on leave_id
        leave = Leave.objects.get(id=leave_id)

        # Update the leave status (change it according to your logic)
        leave.status = 'Approved'
        leave.save()

        messages.success(request, 'Leave status updated successfully!')

    return redirect('view_leaves')  # Redirect back to the view_leaves page

@login_required(login_url='/authentication/login')
def my_leaves(request):
    if request.method == 'GET':
        user_leaves = Leave.objects.filter(user=request.user)
        return render(request, 'leaves/my_leaves.html', {'user_leaves': user_leaves})



