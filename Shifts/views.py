from django.contrib.auth import authenticate, login, logout
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
from .models import shiftSubmitTwo
from .forms import shiftSubmitTwoForm

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
            return redirect("Shifts:index")
        else:
            return render(request, "Shifts/login.html", {"message": "Invalid Input."})

    return render(request, "Shifts/login.html")


# logout user page
def logout_view(request):
    user_name = request.user.username  # get user name before logout
    logout(request)
    return render(
        request, "Shifts/login.html", {"message": f" {user_name} Logged out."}
    )


# adding shifts/ updating weekly shifts (if they exsit)
# the shifts contain the praiorities of the user as well as creation/update data
@login_required()
def add_shifts(request):

    if request.method == "POST":

        weekly_user_shift = get_weekly_user_shifts(request)
        # if weekly shift from user doesn't exist create a new form
        if weekly_user_shift == None:
            form = shiftSubmitTwoForm(request.POST)
        # update the weekly shifts
        else:
            form = shiftSubmitTwoForm(request.POST, instance=weekly_user_shift)

        if form.is_valid():
            # adding authenticed user into the model
            # login is required so  user always not null
            shift_submit = form.save(commit=False)
            shift_submit.user_name = request.user
            shift_submit.save()

        else:
            return render(request, "Shifts/addshifts.html", {"form": form})

    # landing page before POST
    # to do here
    return render(request, "Shifts/addshifts.html", {"form": shiftSubmitTwoForm()})


# returns user weekly shift from the database
def get_weekly_user_shifts(request):
    # calculating this week
    week_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    # for a week that starts on a Sunday
    week_start -= timedelta(days=(week_start.weekday() + 1) % 7)
    # print(f' the time is: {week_start}')  DEBUG
    # 7 days for satruday week-end change to 5 if you want untll thorsday
    week_end = week_start + timedelta(days=7)
    # print(f' the time end : {week_end}') DEBUG
    return shiftSubmitTwo.objects.filter(
        user_name=request.user, created_at__gte=week_start, created_at__lt=week_end
    ).last()


# shows user weekly shift if available, otherwise redirects to adding shift
@login_required()
def myweekshift(request):
    user_shift_result = get_weekly_user_shifts(request)
    # if weekly shift from user doesn't exist redireact to add shift
    if user_shift_result == None:
        # msg of error no shift schedule
        messages.error(request, f"{request.user} has no weekly shifts schedule.")
        return redirect("Shifts:addshifts")

    return render(request, "Shifts/myweekshift.html", {"user_shift": user_shift_result})


# all Shifts display for staff
# optional pass up to days ago to get all shifts up to x days ago from now
@staff_member_required()
def all_shifts(request, up_to_days_ago=None):

    if (
        not up_to_days_ago == None
    ):  # if up_to_days_ago exsits than query  up to x days ago from now
        time_threshold = timezone.now() - timedelta(days=up_to_days_ago)
        all_shift_res = shiftSubmitTwo.objects.filter(
            created_at__gte=time_threshold
        )  # filter query up to x days ago from now
    else:
        all_shift_res = shiftSubmitTwo.objects.all()
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
        user_shift_result = shiftSubmitTwo.objects.filter(
            user_name=f"{uid.id}", created_at__gte=time_threshold
        )
    else:  # display of all the user shifts
        user_shift_result = shiftSubmitTwo.objects.filter(
            user_name=f"{uid.id}"
        )  # filter with id of user

    return render(
        request,
        "Shifts/user_shifts.html",
        {"shift": user_shift_result, "user_name": user_name},
    )
