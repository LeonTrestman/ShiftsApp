from django.urls import path

from . import views


app_name="Shifts"

urlpatterns =[
    path("", views.index, name="index"),
    path("addshift/", views.addshift, name="addshift"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name ="logout"),
    path("allshifts/", views.all_shifts, name="all_shifts"),
    path("myweekshift/", views.myweekshift ,name ="my_weeks_shift" ),
    path("all_shifts/<int:up_to_days_ago>", views.all_shifts, name="all_shifts"),
    path("<str:user_name>/" , views.user_shifts,name ="user shifts"),
    path("<str:user_name>/<int:up_to_days_ago>" , views.user_shifts ,name ="user shifts up to days ago"),
    
]

