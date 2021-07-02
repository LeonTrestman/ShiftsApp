
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from Shifts.forms import shiftSubmitTwoForm
from Shifts.models import shiftSubmitTwo
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
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
@login_required()
def addshift (request):

    if request.method == "POST":
        form = shiftSubmitTwoForm(request.POST)
        

        if form.is_valid():
            #adding authenticed user into the model 
            #login is required so  user always not null
            shift_submit = form.save(commit=False) 
            shift_submit.user_name  = request.user
            shift_submit.save() 
            
        else:
             return render(request,"Shifts/addshift.html",{
                 "form": form
              })

    #landing page before POST
    return render(request,"Shifts/addshift.html",{
        "form": shiftSubmitTwoForm()
    })

#changeing the weekly shift
#if user has no weekly shift,he will be redriected to adding shhift with a msg of no weekly shifts
@login_required()
def myweekshift(request):

    #calculating this week
    week_start = timezone.now()
    week_start -= timedelta(days=(week_start.weekday()-1)%7) #for a week that starts on a Sunday
    week_end = week_start + timedelta(days=7) #7 days for satruday week-end change to 5 if you want untll thorsday
    user_shift_result = shiftSubmitTwo.objects.filter(user_name =request.user, created_at__gte=week_start,
        created_at__lt=week_end ).last()
    if  user_shift_result == None:# if weekly shift from user doesn't exist redireact to add shift
            messages.error(request,f"{request.user} has no weekly shifts schedule.") #msg of error no shift schedule
            return redirect("Shifts:addshift")

    return render(request,"Shifts/myweekshift.html",{
                "user_shift":user_shift_result
        })


#
#todo chhange my weekly shift 
#


#all Shifts display for staff 
#optional pass up to days ago to get all shifts up to x days ago from now 
@staff_member_required() 
def all_shifts(request,up_to_days_ago=None):

    if (not up_to_days_ago == None): #if up_to_days_ago exsits than query  up to x days ago from now
        time_threshold = timezone.now() - timedelta(days=up_to_days_ago)
        all_shift_res=shiftSubmitTwo.objects.filter(created_at__gte = time_threshold)#filter query up to x days ago from now
    else:
        all_shift_res=shiftSubmitTwo.objects.all()
    return render(request,"Shifts/all_shifts.html",{
            "all_shifts":all_shift_res
    })



#return all shifts of certain user by his name
#optional pass up to days ago to get all shifts from user up to x days ago from now 
@staff_member_required() 
def user_shifts(request,user_name,up_to_days_ago=None):
    uid= get_object_or_404(User,username=f"{user_name}") #get user by user_name or raise 404 if doesn't exsit
    if ( not up_to_days_ago == None  ):#if up_to_days_ago exsits than query up to x days ago from now
        time_threshold = timezone.now() - timedelta(days=up_to_days_ago)
        user_shift_result= shiftSubmitTwo.objects.filter(user_name =f"{uid.id}", created_at__gte = time_threshold  ) 
    else:#display of all the user shifts
        user_shift_result= shiftSubmitTwo.objects.filter(user_name =f"{uid.id}" ) #filter with id of user 

    
    return render(request,"Shifts/user_shifts.html", {
        "shift": user_shift_result, 
        "user_name" :user_name      
    })


