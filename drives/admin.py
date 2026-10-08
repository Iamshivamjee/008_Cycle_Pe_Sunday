from django.contrib import admin
from .models import SundayDrive

@admin.register(SundayDrive)
class SundayDriveAdmin(admin.ModelAdmin):
    list_display = ('drive_number', 'date', 'title', 'status')
    list_filter = ('status',)
    
    fieldsets = (
        ('Core Info', {
            'fields': ('drive_number', 'date', 'status')
        }),
        ('Event Details', {
            'fields': ('title', 'description', 'meeting_point', 'end_point', 'start_location_link', 'end_location_link')
        }),
        ('Impact Metrics', {
            'fields': ('primary_activity', 'distance_km', 'trees_planted', 'waste_cleared_kg', 'volunteer_count')
        }),
    )