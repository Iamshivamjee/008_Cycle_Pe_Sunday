from django.db import models

class SundayDrive(models.Model):
    SCHEDULED = 'Scheduled'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'
    
    STATUS_CHOICES = [
        (SCHEDULED, 'Scheduled'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]

    drive_number = models.IntegerField(unique=True)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SCHEDULED)

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    
    # Updated Location Fields
    meeting_point = models.CharField(max_length=255, help_text="e.g., 'Cubbon Park Entrance'")
    end_point = models.CharField(max_length=255, blank=True, null=True, help_text="End location text, e.g., 'Lalbagh Botanical Garden'. Leave blank for a single-location drive.")
    start_location_link = models.URLField(max_length=500, blank=True, null=True, help_text="Paste the Google Maps Share Link for the start.")
    end_location_link = models.URLField(max_length=500, blank=True, null=True, help_text="Paste the Google Maps Share Link for the end (if different).")

    primary_activity = models.CharField(max_length=50)
    distance_km = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    trees_planted = models.IntegerField(default=0)
    waste_cleared_kg = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    volunteer_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Week {self.drive_number}: {self.title}"