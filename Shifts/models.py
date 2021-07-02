from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.

class shiftSubmitTwo(models.Model):
    
    #values for avilability 
    min_val_shift = 0
    max_val_shift = 3

    #on delete of user i still want to keep the old user shifts
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="shift_submitter", on_delete=models.DO_NOTHING)
    sunday_first = models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    sunday_second= models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    monday_first = models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    monday_second= models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    tuesday_first = models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    tuesday_second= models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    wednesday_first = models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    wednesday_second= models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    thursday_first = models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    thursday_second= models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    friday_first = models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    friday_second= models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    saturday_first = models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    saturday_second= models.IntegerField(validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""name: {self.user_name}\n
                   sunday: {self.sunday_first} ,{self.sunday_second}\n
                   monday: {self.monday_first} ,{self.monday_second}\n
                   tuesday: {self.tuesday_second} ,{self.tuesday_second}\n
                   wednesday: {self.wednesday_first} ,{self.thursday_second}\n
                   thursday: {self. friday_first} ,{self. friday_second}\n
                   saturday: {self.saturday_first} ,{self.saturday_second}\n
                   created_at: {self.created_at.strftime("%m/%d/%Y , %H:%M:%S")}\n
                   updated_at: {self.updated_at.strftime("%m/%d/%Y , %H:%M:%S")}\n
                                                                             """