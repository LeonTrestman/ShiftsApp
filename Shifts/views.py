
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth.decorators import login_required


class NewShiftForm(forms.Form):
    sunday=forms.IntegerField(label="Sunday",min_value=0,max_value=3)
    monday=forms.IntegerField(label="monday",min_value=0,max_value=3)
    tuesday=forms.IntegerField(label="tuesday",min_value=0,max_value=3)
    wednesday=forms.IntegerField(label="wednesday",min_value=0,max_value=3)
    thursday=forms.IntegerField(label="thursday",min_value=0,max_value=3)
    friday=forms.IntegerField(label="friday",min_value=0,max_value=3)
    saturday=forms.IntegerField(label="saturday",min_value=0,max_value=3)

# Create your views here.
def index (request):

    if not request.user.is_authenticated:
      return redirect("Shifts:login")
    
    return render(request,"Shifts/index.html")
    

def login_view(request):

    if request.method =="POST":
        username = request.POST["username"] 
        password = request.POST["password"]
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("Shifts:index")
        else:
            return render(request,"Shifts/login.html",{
                "message": "Invalid Input."
            })

    return render(request,"Shifts/login.html")


def logout_view(request):
    logout(request)
    return render(request,"Shifts/login.html",{
        "message":"Logged out."
    })


@login_required(login_url="Shifts:login")
def addshift (request):
    return render(request,"Shifts/addshift.html",{
        "form": NewShiftForm()
    })