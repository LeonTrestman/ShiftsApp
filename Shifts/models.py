from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.

DAYS_OF_WEEK= ["sunday" , "monday" , "tuesday","wednesday","thursday","friday","saturday"]


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
        return f"""name: {self.user_name}
                   sunday: {self.sunday_first} ,{self.sunday_second}
                   monday: {self.monday_first} ,{self.monday_second}
                   tuesday: {self.tuesday_second} ,{self.tuesday_second}
                   wednesday: {self.wednesday_first} ,{self.thursday_second}
                   thursday: {self. friday_first} ,{self. friday_second}
                   saturday: {self.saturday_first} ,{self.saturday_second}
                   created_at: {self.created_at.strftime("%d/%m/%Y , %H:%M:%S")}
                   updated_at: {self.updated_at.strftime("%d/%m/%Y , %H:%M:%S")}
                                                                             """

## add table of shift per user on week

class weekly_schedule(models.Model):
    sunday_first_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sunday_first_user", on_delete=models.DO_NOTHING)
    sunday_second_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sunday_second_user", on_delete=models.DO_NOTHING)
    monday_first_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="monday_first_user", on_delete=models.DO_NOTHING)
    monday_second_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name="monday_second_user", on_delete=models.DO_NOTHING)
    tuesday_first_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="tuesday_first_user", on_delete=models.DO_NOTHING)
    tuesday_second_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name="tuesday_second_user", on_delete=models.DO_NOTHING)
    wednesday_first_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="wednesday_first_user", on_delete=models.DO_NOTHING)
    wednesday_second_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name="wednesday_second_user", on_delete=models.DO_NOTHING)
    thursday_first_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="thursday_first_user", on_delete=models.DO_NOTHING)
    thursday_second_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="thursday_second_user", on_delete=models.DO_NOTHING)
    friday_first_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="friday_first_user", on_delete=models.DO_NOTHING)
    friday_second_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name="friday_second_user", on_delete=models.DO_NOTHING)
    saturday_first_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="saturday_first_user", on_delete=models.DO_NOTHING)
    saturday_second_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name="saturday_second_user", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""week : {self.created_at.strftime("%U")}\n
                   sunday: {self.sunday_first_user} ,{self.sunday_second_user}\n
                   monday: {self.monday_first_user} ,{self.monday_second_user}\n
                   tuesday: {self.tuesday_second_user} ,{self.tuesday_second_user}\n
                   wednesday: {self.wednesday_first_user} ,{self.thursday_second_user}\n
                   thursday: {self. friday_first_user} ,{self. friday_second_user}\n
                   saturday: {self.saturday_first_user} ,{self.saturday_second_user}\n
                   created_at: {self.created_at.strftime("%d/%m/%Y , %H:%M:%S")}\n
                   updated_at: {self.updated_at.strftime("%d/%m/%Y , %H:%M:%S")}\n
                                                                             """