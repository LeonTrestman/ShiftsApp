from django import forms
from django.forms import ModelForm
from .models import shiftSubmitTwo, weekly_schedule
from .consts import DAYS_OF_WEEK,TYPE_OF_SHIFTS

# class NewShiftForm(forms.Form):
#     sunday=forms.IntegerField(label="Sunday",min_value=0,max_value=3)
#     monday=forms.IntegerField(label="monday",min_value=0,max_value=3)
#     tuesday=forms.IntegerField(label="tuesday",min_value=0,max_value=3)
#     wednesday=forms.IntegerField(label="wednesday",min_value=0,max_value=3)
#     thursday=forms.IntegerField(label="thursday",min_value=0,max_value=3)
#     friday=forms.IntegerField(label="friday",min_value=0,max_value=3)
#     saturday=forms.IntegerField(label="saturday",min_value=0,max_value=3)




class shiftSubmitTwoForm (ModelForm):
    class Meta:
        model = shiftSubmitTwo
        exclude = ['user_name']

        widgets={}
        for day in DAYS_OF_WEEK:
            for shift_type in TYPE_OF_SHIFTS:
                widgets[f'{day}_{shift_type}'] =forms.NumberInput(attrs={'class': 'form-control'})        

class weekly_schedule_Form (ModelForm):
    class Meta:
        model = weekly_schedule
        fields = '__all__'