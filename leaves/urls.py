
from django.urls import path
from . import views

urlpatterns = [
    path('leave-request/', views.leave_request_view, name='leave_request'),
    path('my-leaves/', views.leave_request_list, name='leave_request_list'),
    path('manage-leaves/', views.manage_leave_requests, name='manage_leave_requests'),
    path('approve-leave/<int:request_id>/', views.approve_leave, name='approve_leave'),
    path('reject-leave/<int:request_id>/', views.reject_leave, name='reject_leave'),
]
