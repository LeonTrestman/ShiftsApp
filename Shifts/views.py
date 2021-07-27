from Shifts.myFunctions import calc_next_week, calc_start_week
from django.contrib.auth import authenticate, login, logout
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
from .models import WeeklyDayDates, WeeklyUserSchedule
from .forms import WeeklyUserScheduleForm

# index page
def index(request):

    return render(request, "Shifts/index.html")


# login user page
def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,  f"{request.user} sucssesfully logged in")
            return redirect("Shifts:index")
        else:
            messages.error(request, f"Invalid login,Please try again")
            

    return render(request, "Shifts/login.html")


# logout user 
def logout_view(request):
    user_name = request.user.username  # get user name before logout
    logout(request)
    messages.success(request,  f" {user_name} logged out.")
    return render(
        request, "Shifts/login.html"
    )


# adding shifts/ updating weekly shifts (if they exsit)
# check if weekly shift is avaliable and updates or creates one
# the shifts contain the praiorities of the user as well as creation/update data

@login_required()
def add_shifts(request):

    WeeklyUserSchedule = get_WeeklyUserSchedule(request) 


    # if weekly shift from user doesn't exist create a new form
    if WeeklyUserSchedule == None:
        form = WeeklyUserScheduleForm()
        
    # update the weekly shifts values
    else:
        form = WeeklyUserScheduleForm(instance=WeeklyUserSchedule)


    if request.method == "POST":

        ##handling creation or fatching the next week WeeklyDayDates
        Weekly_Day_Dates = get_next_week_WeeklyDayDates(request)# get next week WeeklyDayDates
        #create one if WeeklyDayDates not exsits
        if not Weekly_Day_Dates : 
            Weekly_Day_Dates = WeeklyDayDates()
            Weekly_Day_Dates.save()


        #changes  the last week shifts (creates or updates)
        form = WeeklyUserScheduleForm(request.POST, instance=WeeklyUserSchedule)
        if form.is_valid():
            # adding authenticed user into the model
            # login is required so user always not null
            shift_submit = form.save(commit=False)
            shift_submit.user_name = request.user
            shift_submit.WeeklyDayDates = Weekly_Day_Dates
            shift_submit.save()
            
            messages.success(request, 'Shift schedule have been changed.')
            
        ######################################################

        else:
            messages.error(request,"Error,Form isn't valid")
            

    context = {"form": form}
    add_weekdays_to_context_form(context,form)
    return render(request, "Shifts/addshifts.html", context)


#returns next week WeeklyDayDates (from next week sunday)
def get_next_week_WeeklyDayDates(request):
    return WeeklyDayDates.objects.filter(
        sunday_date=calc_next_week() #for the next week synday
    ).last()


# returns user weekly shift from the database
def get_WeeklyUserSchedule(request):
    week_start = calc_start_week()
    week_end = calc_next_week()
    print (week_end)
    return WeeklyUserSchedule.objects.filter(
        user_name=request.user, created_at__gte=week_start, created_at__lt=week_end
    ).last()


###################################################will be deleted
#adds to context all days of week to pass of model
def add_weekdays_to_context_model(context, model):
    for i in range(0,7):
        context[f"date{i}"] = model.day_date(i)

#adds to context all days of week to pass of form
def add_weekdays_to_context_form(context, form):
    for i in range(0,7):
        context[f"date{i}"] = form.day_date(i)
###########################################################################

# shows user weekly shift if available, otherwise redirects to adding shift
@login_required()
def my_schedule(request):
    user_shift_result = get_WeeklyUserSchedule(request)
    # if weekly shift from user doesn't exist redireact to add shift
    if user_shift_result == None:
        # msg of error no shift schedule
        messages.error(request, f"{request.user} has no weekly shifts schedule.")
        return redirect("Shifts:addshifts")
    context = {"user_shift": user_shift_result}
    add_weekdays_to_context_model (context,user_shift_result)
    return render(request, "Shifts/myschedule.html", context)

# shows user all weekly shift schedules for the week
########add weeks ago
@login_required()
def Weekly_schedules(request , week_ago= None):
    week_start= calc_next_week()
    Weekly_schedules_res = WeeklyDayDates.objects.filter(sunday_date = week_start).last()
    Weekly_schedules_res = Weekly_schedules_res.UserSchedule.all()

    context = {"Weekly_schedules": Weekly_schedules_res}
   
    return render(
        request,
        "Shifts/weeklyschedules.html",
        context
    )

# all Shifts display for staff
# optional pass up to days ago to get all shifts up to x days ago from now
@staff_member_required()
def all_shifts(request, up_to_days_ago=None):

    if (
        not up_to_days_ago == None
    ):  # if up_to_days_ago exsits than query  up to x days ago from now
        time_threshold = timezone.now() - timedelta(days=up_to_days_ago)
        all_shift_res = WeeklyUserSchedule.objects.filter(
            created_at__gte=time_threshold
        )  # filter query up to x days ago from now
    else:
        all_shift_res = WeeklyUserSchedule.objects.all()
    return render(request, "Shifts/all_shifts.html", {"all_shifts": all_shift_res})


# returns user by user_name or raise 404 if doesn't exsit
def get_uid_by_name(user_name):
    return get_object_or_404(User, username=f"{user_name}")


# return all shifts of certain user by his name
# only staff/admin and the user itself can see their shift history
# optional pass up to days ago to get all shifts from user up to x days ago from now
@login_required()
def user_shifts(request, user_name, up_to_days_ago=None):

    # only staff/admin and the user it self can see their shift history
    if not request.user.is_staff and request.user.username != user_name:
        raise Http404('Error, user name does\'nt match ')

    # getting the user by name
    uid = get_uid_by_name(user_name)
    if (
        not up_to_days_ago == None
    ):  # if up_to_days_ago exsits than query up to x days ago from now
        time_threshold = timezone.now() - timedelta(days=up_to_days_ago)
        user_shift_result = WeeklyUserSchedule.objects.filter(
            user_name=f"{uid.id}", created_at__gte=time_threshold
        )
    else:  # display of all the user shifts
        user_shift_result = WeeklyUserSchedule.objects.filter(
            user_name=f"{uid.id}"# filter with id of user
        ).order_by('-created_at')  #oreder by the newest

    #if there is no history display eror msg
    if not user_shift_result  :
        messages.error(request,"There are no past submissions ")

    context = {"shifts": user_shift_result}
   

    return render(
        request,
        "Shifts/user_shifts.html",
        context
    )
