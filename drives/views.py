from django.shortcuts import render
from django.db.models import Sum, Max, DecimalField
from django.db.models.functions import Coalesce
from decimal import Decimal
from .models import SundayDrive

def homepage_view(request):
    next_drive = SundayDrive.objects.filter(status=SundayDrive.SCHEDULED).order_by('date').first()
    completed_drives = SundayDrive.objects.filter(status=SundayDrive.COMPLETED)
    
    impact = completed_drives.aggregate(
        total_weeks=Max('drive_number'),
        total_trees=Coalesce(Sum('trees_planted'), 0),
        total_waste_kg=Coalesce(Sum('waste_cleared_kg'), Decimal('0.0'), output_field=DecimalField()),
        total_volunteers=Coalesce(Sum('volunteer_count'), 0)
    )

    return render(request, 'homepage.html', {'next_drive': next_drive, 'impact': impact})

def impact_archive_view(request):
    past_drives = SundayDrive.objects.filter(status=SundayDrive.COMPLETED)
    return render(request, 'impact.html', {'past_drives': past_drives})

def about_view(request):
    return render(request, 'about.html')

def join_view(request):
    return render(request, 'join.html')