from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.

class shiftSubmitTwo(models.Model):
    
    #values for avilability 
    minvalshift = 0
    maxvalshift = 3

    #on delete of user i still want to keep the old user shifts
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="shift_submitter", on_delete=models.DO_NOTHING)
    sunday_first = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    sunday_second= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    monday_first = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    monday_second= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    tuesday_first = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    tuesday_second= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    wednesday_first = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    wednesday_second= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    thursday_first = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    thursday_second= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    friday_first = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    friday_second= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    saturday_first = models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    saturday_second= models.IntegerField(validators=[MinValueValidator(minvalshift),MaxValueValidator(maxvalshift)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""name: {self.user_name}
                   sunday:{self.sunday_first} ,{self.sunday_second}\n
                   monday:{self.monday_first} ,{self.monday_second}\n
                   tuesday:{self.tuesday_second} ,{self.tuesday_second}\n
                   wednesday:{self.wednesday_first} ,{self.thursday_second}\n
                   thursday:{self. friday_first} ,{self. friday_second}\n
                   saturday:{self.saturday_first} ,{self.saturday_second}\n
                   created_at:{self.created_at}\n
                   updated_at:{self.updated_at}\n
                                                                             """