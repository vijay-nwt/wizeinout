from django.contrib import admin
from .models import Employee ,PunchRecord # Import your Employee model

# Create an admin class to customize the admin panel
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address', 'date_of_joining','is_active')  # Fields to display in the list view
    search_fields = ('name', 'email')  # Fields to search in the admin panel
    list_filter = ('date_of_joining',)  # Filters to apply on the list view

# Register the Employee model with the admin site
admin.site.register(Employee, EmployeeAdmin)



# Register the PunchRecord model in the admin panel
@admin.register(PunchRecord)
class PunchRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'punch_in_time', 'punch_out_time', 'date')
    list_filter = ('employee', 'date')
    search_fields = ('employee__name',)
    ordering = ('-date',)