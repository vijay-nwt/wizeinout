
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, PunchRecord , User
from django.contrib.auth.decorators import login_required
import datetime
from datetime import timedelta
import pytz

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == 'POST':
        # Collect form data and save new employee
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        date_of_joining = request.POST['date_of_joining']
        user = request.user  #flag
        # Assuming user and authentication setup is in place
        Employee.objects.create(user=user,name=name, email=email, phone=phone, address=address, date_of_joining=date_of_joining)
        return redirect('employee_list')
    return render(request, 'add_employee.html')

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.address = request.POST['address']
        employee.date_of_joining = request.POST['date_of_joining']
        employee.save()
        return redirect('employee_list')
    return render(request, 'edit_employee.html', {'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employee_list')

@login_required
def punch_in_out(request):
    return render(request, 'punch_in_out.html')

# @login_required
# def punch_in(request):
#     employee = request.user.employee
#     today = datetime.date.today()
#     punch_record, created = PunchRecord.objects.get_or_create(employee=employee, date=today)
#     if not punch_record.punch_in_time:
#         punch_record.punch_in_time = datetime.datetime.now()
#         punch_record.save()
#         message = "Punched In successfully!" 
#     else:
#         message = f"Already Punched In for today at {punch_record.punch_in_time}."
#     return render(request, 'punch_in_out.html', {'message': message})

from django.shortcuts import redirect
from django.contrib import messages
import datetime
from .models import PunchRecord

@login_required
def punch_in(request):
    try:
        # Check if the user has an associated employee
        employee = request.user.employee
    except Employee.DoesNotExist:
        # Redirect to the "Add Employee" page if the user doesn't have an employee record
        messages.error(request, "Please add your employee details before punching in.")
        return redirect('add_employee')

    # Proceed with punch-in logic if the employee exists
    today = datetime.date.today()
    punch_record, created = PunchRecord.objects.get_or_create(employee=employee, date=today)

    ist = pytz.timezone('Asia/Kolkata')

    if not punch_record.punch_in_time:
        punch_record.punch_in_time = datetime.datetime.now(ist)
        punch_record.save()
        formatted_time = punch_record.punch_in_time.strftime('%d-%m-%Y %I:%M %p').replace("AM", "a.m.").replace("PM", "p.m.")

        message = f"Punched In successfully at {formatted_time}" 
    else:
        # formatted_time = punch_record.punch_in_time.strftime('%d-%m-%Y %H:%M:%S')
        # formatted_time = punch_record.punch_in_time.strftime('%d-%m-%Y %I:%M %p').replace("AM", "a.m.").replace("PM", "p.m.")
        
        formatted_time = (punch_record.punch_in_time + timedelta(hours=5, minutes=30)).strftime('%d-%m-%Y %I:%M %p').replace("AM", "a.m.").replace("PM", "p.m.")


        message = f"Already Punched In for today at {formatted_time}."
    
    return render(request, 'punch_in_out.html', {'message': message})


# @login_required
# def punch_in(request):
#     try:
#         # Attempt to get the employee associated with the logged-in user
#         employee = request.user.employee  # Adjust this line if your relationship is different
#     except Employee.DoesNotExist:
#         messages.error(request, "You need to create an employee record before punching in.")
#         return redirect('add_employee')  # Redirect to add employee page

#     # Handle the punch-in logic if employee exists
#     if request.method == 'POST':
#         # Create or update the punch record
#         punch_record, created = PunchRecord.objects.get_or_create(
#             employee=employee,
#             date=datetime.date.today(),
#             defaults={'punch_in_time': timezone.now()}
#         )
#         if not created:
#             # Update the existing record's punch_in_time if necessary
#             punch_record.punch_in_time = timezone.now()
#             punch_record.save()
        
#         messages.success(request, "Punched in successfully.")
#         return redirect('punch_in_out')  # Redirect to punch in/out page

#     return render(request, 'punch_in.html')  # Render punch-in page

# @login_required
# def punch_out(request):
#     employee = request.user.employee
#     today = datetime.date.today()
#     try:
#         punch_record = PunchRecord.objects.get(employee=employee, date=today)
#         if punch_record.punch_in_time and not punch_record.punch_out_time:
#             punch_record.punch_out_time = datetime.datetime.now()
#             punch_record.save()
#             message = "Punched Out successfully!"
#         else:
#             message = f"Already Punched Out for today at {punch_record.punch_out_time}"
#     except PunchRecord.DoesNotExist:
#         message = "No Punch In record found for today."
#     return render(request, 'punch_in_out.html', {'message': message})

@login_required
def punch_out(request):
    try:
        employee = request.user.employee
    except Employee.DoesNotExist:
        messages.error(request, "Please add your employee details before punching out.")
        return redirect('add_employee')

    today = datetime.date.today()
    try:
        punch_record = PunchRecord.objects.get(employee=employee, date=today)

        ist = pytz.timezone('Asia/Kolkata')

        if punch_record.punch_in_time and not punch_record.punch_out_time:
            punch_record.punch_out_time = datetime.datetime.now(ist)
            punch_record.save()
            formatted_time = punch_record.punch_out_time.strftime('%d-%m-%Y %I:%M %p').replace("AM", "a.m.").replace("PM", "p.m.")
            message = f"Punched Out successfully at {formatted_time}"
        else:
            # formatted_time = punch_record.punch_out_time.strftime('%d-%m-%Y %I:%M %p').replace("AM", "a.m.").replace("PM", "p.m.")
            formatted_time = (punch_record.punch_out_time + timedelta(hours=5, minutes=30)).strftime('%d-%m-%Y %I:%M %p').replace("AM", "a.m.").replace("PM", "p.m.")

            message = f"You have already punched out at {formatted_time}."
    except PunchRecord.DoesNotExist:
        message = "You haven't punched in today."

    return render(request, 'punch_in_out.html', {'message': message, 'punched_in': False})



# Sign-Up View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful sign-up
            messages.success(request, 'Account created successfully!')
            return redirect('login')  
        else:
            print('finding error',form.errors)
            messages.error(request, 'Sign-up failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# Login View
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Welcome back, {username}!")
#                 return redirect('punch_in_out') 
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                
                # Check if the user has an associated Employee record
                if Employee.objects.filter(user=user).exists():
                    return redirect('punch_in_out')  # Redirect to punch in/out page
                else:
                    return redirect('add_employee')  # Redirect to add employee page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



# Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Redirect to the login page after logout
