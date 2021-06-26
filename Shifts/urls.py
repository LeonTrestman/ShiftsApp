from django.urls import path

from . import views

app_name="Shifts"

urlpatterns =[
    path("", views.index, name="index"),
    path("addshift", views.addshift, name="addshift")
]