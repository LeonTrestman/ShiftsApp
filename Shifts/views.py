
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from . import forms 
from Shifts.models import shiftSubmitTwo

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
    user_name= request.user.username #get user name before logout
    logout(request)
    return render(request,"Shifts/login.html",{
        "message":f" {user_name} Logged out."
    })


#adding shift to the database 
#the shift contains name and a week schedule of the worker
@login_required(login_url="Shifts:login")
def addshift (request):

    if request.method == "POST":
        form = forms.shiftSubmitTwoForm(request.POST)
        

        if form.is_valid():
            #adding authenticed user into the model 
            #login is required so cannot user always not null
            shift_submit = form.save(commit=False) 
            shift_submit.user_name  = request.user
            shift_submit.save() 
            
        else:
             return render(request,"Shifts/addshift.html",{
                 "form": form
              })

    #landing page before POST
    return render(request,"Shifts/addshift.html",{
        "form": forms.shiftSubmitTwoForm()
    })


#all Shifts display for staff 
@staff_member_required(login_url="Shifts:login") 
def all_shifts(request):
    return render(request,"Shifts/all_shifts.html",{
            "all_shifts":shiftSubmitTwo.objects.all()
    })


#TO Do : add if user doesnt exist 
#return all shifts of certain user by his name
@staff_member_required(login_url="Shifts:login") 
def user_shifts(request,user_name):
    uid = User.objects.get(username=f"{user_name}") #get usr by the user_name provided
    user_shift_result= shiftSubmitTwo.objects.filter(user_name =f"{uid.id}" ) #filter with id of user
    return render(request,"Shifts/user_shifts.html", {
        "shift": user_shift_result
    })

    

