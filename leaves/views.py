from django.shortcuts import render

# Create your views here.
# views.py

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import LeaveRequest
from django.contrib import messages

@login_required
def leave_request_view(request):
    """Employee view to submit a leave request using HTML form."""
    if request.method == 'POST':
        # Extract data from the HTML form
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        # Basic validation (you can add more validations as needed)
        if not start_date or not end_date or not reason:
            messages.error(request, "All fields are required!")
        else:
            # Create and save the leave request
            LeaveRequest.objects.create(
                employee=request.user,
                start_date=start_date,
                end_date=end_date,
                reason=reason,
                status='Pending'
            )
            messages.success(request, "Leave request submitted successfully!")
            return redirect('leave_request_list')

    return render(request, 'leave_request_form.html')

@login_required
def leave_request_list(request):
    """Employee view to see their own leave requests."""
    leave_requests = LeaveRequest.objects.filter(employee=request.user)
    return render(request, 'leave_request_list.html', {'leave_requests': leave_requests})

@user_passes_test(lambda u: u.is_superuser)
def manage_leave_requests(request):
    """Superuser view to see all leave requests and approve/reject them."""
    leave_requests = LeaveRequest.objects.filter(status='Pending')
    return render(request, 'manage_leave_requests.html', {'leave_requests': leave_requests})

@user_passes_test(lambda u: u.is_superuser)
def approve_leave(request, request_id):
    """Superuser view to approve a leave request."""
    leave_request = get_object_or_404(LeaveRequest, id=request_id)
    leave_request.status = 'Approved'
    leave_request.approved_by = request.user
    leave_request.save()
    return redirect('manage_leave_requests')

@user_passes_test(lambda u: u.is_superuser)
def reject_leave(request, request_id):
    """Superuser view to reject a leave request."""
    leave_request = get_object_or_404(LeaveRequest, id=request_id)
    leave_request.status = 'Rejected'
    leave_request.approved_by = request.user
    leave_request.save()
    return redirect('manage_leave_requests')
