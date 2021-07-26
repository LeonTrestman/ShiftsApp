from django.contrib import admin
from .models import WeeklyUserSchedule, WeeklyDayDates, WeeklySchedule

# Register your models here.
admin.site.register(WeeklyUserSchedule)
admin.site.register(WeeklySchedule)
admin.site.register(WeeklyDayDates)