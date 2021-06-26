from django.urls import path

from . import views
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

app_name="Shifts"

urlpatterns =[
    path("", views.index, name="index"),
    path("addshift", views.addshift, name="addshift")
]

urlpatterns += staticfiles_urlpatterns()