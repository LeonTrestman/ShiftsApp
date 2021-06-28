from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.

class shiftSubmitTwo(models.Model):
    #on delete of user i still want to keep the old user shifts
    userName = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="shift_submitter", on_delete=models.DO_NOTHING)
    sundayFirst = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    sundaySecond= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    mondayFirst = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    mondaySecond= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    tuesdayFirst = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    tuesdaySecond= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    wednesdayFirst = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    wednesdaySecond= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    thursdayFirst = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    thursdaySecond= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    fridayFirst = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    fridaySecond= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    saturdayFirst = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])
    saturdaySecond= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(3)])

    def __str__(self):
        return f"""sunday:{self.sundayFirst} ,{self.sundaySecond}\n
                   monday:{self.mondayFirst} ,{self.mondaySecond}\n
                   tuesday:{self.tuesdayFirst} ,{self.tuesdaySecond}\n
                   wednesday:{self.wednesdayFirst} ,{self.wednesdaySecond}\n
                   thursday:{self. thursdayFirst} ,{self. thursdaySecond}\n
                   saturday:{self.saturdayFirst} ,{self.saturdaySecond}\n
                                                                             """