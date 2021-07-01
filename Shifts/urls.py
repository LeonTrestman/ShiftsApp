from django.urls import path

from . import views
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

app_name="Shifts"

urlpatterns =[
    path("", views.index, name="index"),
    path("addshift", views.addshift, name="addshift"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name ="logout"),
    path("all_shifts", views.all_shifts, name="all_shifts"),
    path("<str:user_name>/" , views.user_shifts,name ="user shifts"),
    path("<str:user_name>/<int:up_to_days_ago>" , views.user_shifts ,name ="user shifts up to days ago")
]

