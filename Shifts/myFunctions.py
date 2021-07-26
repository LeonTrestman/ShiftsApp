#returning the sunday date of the curret week
from datetime import timedelta
from django.utils import timezone

#returning the sunday date of the current week
def calc_start_week():
    week_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    # for a week that starts on a Sunday
    week_start -= timedelta(days=(week_start.weekday() + 1) % 7)
    return week_start

#returning the sunday date of the next week
def calc_next_week():
    # calculating this week
    week_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    # for a week that starts on a Sunday
    week_start -= timedelta(days=(week_start.weekday() + 1) % 7)
    # 7 days for satruday week-end change to 5 if you want untll thorsday
    week_end = week_start + timedelta(days=7)
    return week_end