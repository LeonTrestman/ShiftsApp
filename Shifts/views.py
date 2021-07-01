
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from . import forms 
from Shifts.models import shiftSubmitTwo
from datetime import datetime, timedelta
from django.utils import timezone

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
@staff_member_required() 
def all_shifts(request):
    return render(request,"Shifts/all_shifts.html",{
            "all_shifts":shiftSubmitTwo.objects.all()
    })



#return all shifts of certain user by his name
#optional pass up to days ago to get all shifts from user up to x days ago from now 
@staff_member_required() 
def user_shifts(request,user_name,up_to_days_ago=None):
    uid= get_object_or_404(User,username=f"{user_name}") #get user by user_name or raise 404 if doesn't exsit
    if ( not up_to_days_ago == None  ):#if up_to_days_ago exsits than query  up to x days ago from now
        time_threshold = timezone.now() - timedelta(days=up_to_days_ago)
        user_shift_result= shiftSubmitTwo.objects.filter(user_name =f"{uid.id}", created_at__gte = time_threshold  ) 
    else:#display of all the user shifts
        user_shift_result= shiftSubmitTwo.objects.filter(user_name =f"{uid.id}" ) #filter with id of user 

    return render(request,"Shifts/user_shifts.html", {
        "shift": user_shift_result
    })


