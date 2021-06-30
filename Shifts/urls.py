from django.urls import path

from . import views
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

app_name="Shifts"

urlpatterns =[
    path("", views.index, name="index"),
    path("addshift", views.addshift, name="addshift"),
    path("login", views.login_view, name="login"),
    path("logout",views.logout_view, name ="logout"),
    path("all_shifts",views.user_shifts, name="user_shifts")
]

urlpatterns += staticfiles_urlpatterns()