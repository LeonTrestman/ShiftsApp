from django.urls import path

from . import views


app_name="Shifts"

urlpatterns =[
    path("", views.index, name="index"),
    path("addshifts/", views.add_shifts, name="addshifts"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name ="logout"),
    path("allshifts/", views.all_shifts, name="all_shifts"),
    path("myschedule/", views.my_schedule ,name ="my_weekly_schedule" ),
    path("weeklyschedules/", views.Weekly_schedules , name = "Weekly_schedules"),
    path("weeklyschedules/<int:week_ago>", views.Weekly_schedules , name = "Weekly_schedules_ago"),
    path("all_shifts/<int:up_to_days_ago>", views.all_shifts, name="all_shifts"),
    path("<str:user_name>/" , views.user_shifts,name ="user shifts"),
    path("<str:user_name>/<int:up_to_days_ago>" , views.user_shifts ,name ="user_shifts_up_to_days_ago"),
    
]

