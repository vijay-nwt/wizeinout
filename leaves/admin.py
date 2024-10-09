from django.contrib import admin

from .models import LeaveRequest

# Create a custom admin class for the LeaveRequest model
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'status', 'approved_by', 'created_at', 'updated_at')
    search_fields = ('employee__name', 'status')
    list_filter = ('status', 'start_date', 'end_date')
    ordering = ('-created_at',)

# Register the LeaveRequest model with the custom admin class
admin.site.register(LeaveRequest, LeaveRequestAdmin)
