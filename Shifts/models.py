from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.

class shiftSubmitTwo(models.Model):

    #values for avilability 
    minvalshift = 0
    maxvalshift = 3

    #on delete of user i still want to keep the old user shifts
    userName = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="shift_submitter", on_delete=models.DO_NOTHING)
    sundayFirst = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    sundaySecond= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    mondayFirst = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    mondaySecond= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    tuesdayFirst = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    tuesdaySecond= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    wednesdayFirst = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    wednesdaySecond= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    thursdayFirst = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    thursdaySecond= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    fridayFirst = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    fridaySecond= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    saturdayFirst = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    saturdaySecond= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])

    def __str__(self):
        return f"""sunday:{self.sundayFirst} ,{self.sundaySecond}\n
                   monday:{self.mondayFirst} ,{self.mondaySecond}\n
                   tuesday:{self.tuesdayFirst} ,{self.tuesdaySecond}\n
                   wednesday:{self.wednesdayFirst} ,{self.wednesdaySecond}\n
                   thursday:{self. thursdayFirst} ,{self. thursdaySecond}\n
                   saturday:{self.saturdayFirst} ,{self.saturdaySecond}\n
                                                                             """