from django import forms
from django.forms import ModelForm
from Shifts.models import shiftSubmitTwo

class NewShiftForm(forms.Form):
    sunday=forms.IntegerField(label="Sunday",min_value=0,max_value=3)
    monday=forms.IntegerField(label="monday",min_value=0,max_value=3)
    tuesday=forms.IntegerField(label="tuesday",min_value=0,max_value=3)
    wednesday=forms.IntegerField(label="wednesday",min_value=0,max_value=3)
    thursday=forms.IntegerField(label="thursday",min_value=0,max_value=3)
    friday=forms.IntegerField(label="friday",min_value=0,max_value=3)
    saturday=forms.IntegerField(label="saturday",min_value=0,max_value=3)




days= ["Sunday" , "Monday" , "Tuesday","wednesday","thursday"]

class shiftSubmitTwoForm (ModelForm):
    class Meta:
        model = shiftSubmitTwo
        fields = '__all__'