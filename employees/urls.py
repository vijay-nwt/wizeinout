from django.urls import path
from . import views,send_mail

urlpatterns = [
    path('',views.homepage,name='home'),
    path('employee-list/', views.employee_list, name='employee_list'),  # Show employee list
    path('employee/add/', views.add_employee, name='add_employee'),  # Add new employee
    path('employee/edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),  # Edit employee details
    path('employee/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),  # Delete employee
    path('punch_in_out/', views.punch_in_out, name='punch_in_out'),  # Punch In/Out main page
    path('punch_in/', views.punch_in, name='punch_in'),  # Punch In logic
    path('punch_out/', views.punch_out, name='punch_out'),  # Punch Out logic
    path('my-profile',views.myprofile,name='myprofile'),

    path('send-email',send_mail.send_test_email,name='send_email'),
    path('signup-email',send_mail.signup_email,name='signup_email'),

     # Authentication URLs
    path('signup/', views.signup, name='signup'),  # Sign-up page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page
]
