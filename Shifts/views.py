
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms 

# Create your views here.
def index (request):

   # if not request.user.is_authenticated:
     # return redirect("Shifts:login")
    
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

    if request.method == "POST":
        form = forms.shiftSubmitTwoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
             return render(request,"Shifts/addshift.html",{
                 "form": form
              })

    return render(request,"Shifts/addshift.html",{
        "form": forms.shiftSubmitTwoForm()
    })