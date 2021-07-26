from datetime import timedelta
from django import forms
from django.forms import ModelForm
from django.utils import timezone
from .models import shiftSubmitTwo, weekly_schedule
from .consts import DAYS_OF_WEEK, TYPE_OF_SHIFTS,MIN_VAL_SHIFT,MAX_VAL_SHIFT,SUBMIT_CHOICES 

# class NewShiftForm(forms.Form):
#     sunday=forms.IntegerField(label="Sunday",min_value=0,max_value=3)
#     monday=forms.IntegerField(label="monday",min_value=0,max_value=3)
#     tuesday=forms.IntegerField(label="tuesday",min_value=0,max_value=3)
#     wednesday=forms.IntegerField(label="wednesday",min_value=0,max_value=3)
#     thursday=forms.IntegerField(label="thursday",min_value=0,max_value=3)
#     friday=forms.IntegerField(label="friday",min_value=0,max_value=3)
#     saturday=forms.IntegerField(label="saturday",min_value=0,max_value=3)


class shiftSubmitTwoForm(ModelForm):
    class Meta:
        model = shiftSubmitTwo
        exclude = ["user_name"]

        widgets = {}
        for day in DAYS_OF_WEEK:
            for shift_type in TYPE_OF_SHIFTS:
                widgets[f"{day}_{shift_type}"] = forms.Select(
                    choices=SUBMIT_CHOICES,attrs={
                        "class": "form-control-sm",    #for bootstrap 
                        'min' :MIN_VAL_SHIFT,           #validators
                        'max': MAX_VAL_SHIFT
                        }

                )
    def day_date(self,dayindex):
        day = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        ## get the date of the following day index of the creation date
        day -= timedelta(days=(day.weekday() + 1) % 7) # for a week that starts on a Sunday
        day += timedelta(days=7+dayindex )  #adding the following week with dayindex
        return day
    

class weekly_schedule_Form(ModelForm):
    class Meta:
        model = weekly_schedule
        fields = "__all__"
