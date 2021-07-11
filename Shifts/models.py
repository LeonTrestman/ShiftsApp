from .consts import DAYS_OF_WEEK, SHIFTS_HOURS_REG, SHIFTS_HOURS_REG_UNDERSCORE, SHIFTS_HOURS_WEEKENDS, SHIFTS_HOURS_WEEKENDS_UNDERSCORE,TYPE_OF_SHIFTS,MIN_VAL_SHIFT,MAX_VAL_SHIFT
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


# model for user availability for shifts
# this model has 2 shifts for each day in a week


class shiftSubmitTwo(models.Model):
 

    # on deletetion of user his shifts should remain in the database
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="shift_submitter",
        on_delete=models.DO_NOTHING,
    )

    # creating the integerfield of availability of the shifts form user
    for day in DAYS_OF_WEEK:
        #weekends have diffrent hours
        if (day == 'friday' or day == 'saturday'):
            for shift_type,shift_hour in zip(TYPE_OF_SHIFTS,SHIFTS_HOURS_WEEKENDS  ) :

                exec(
                    f'{day}_{shift_type} = models.IntegerField(verbose_name =f"{day} {shift_type} {shift_hour}" ,default=0 ,validators=[MinValueValidator(MIN_VAL_SHIFT),MaxValueValidator(MAX_VAL_SHIFT)])'
                )
                
        else:
            for shift_type,shift_hour in zip(TYPE_OF_SHIFTS,SHIFTS_HOURS_REG ) :

                exec(
                    f'{day}_{shift_type} = models.IntegerField(verbose_name =f"{day} {shift_type} {shift_hour}" ,default=0 ,validators=[MinValueValidator(MIN_VAL_SHIFT),MaxValueValidator(MAX_VAL_SHIFT)])'
                )    
            #TODO: fix here variable name with underscore and label with regular      

            

    # datefields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #TODO:fix #3 str
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


# model for weekly assigments of users to shifts
# this model has 2 shifts each day
class weekly_schedule(models.Model):
    # creating field for user placment for each shift
    for day in DAYS_OF_WEEK:
        for shift_type in TYPE_OF_SHIFTS:
            # on deletetion of user his shifts should remain in the database
            exec(
                f'{day}_{shift_type}_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="{day}_{shift_type}_user", on_delete=models.DO_NOTHING)'
            )

    # datefields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""week : {self.created_at.strftime("%U")} 
                   sunday: {self.sunday_first_user} ,{self.sunday_second_user} 
                   monday: {self.monday_first_user} ,{self.monday_second_user} 
                   tuesday: {self.tuesday_second_user} ,{self.tuesday_second_user} 
                   wednesday: {self.wednesday_first_user} ,{self.thursday_second_user}
                   thursday: {self. friday_first_user} ,{self. friday_second_user}
                   saturday: {self.saturday_first_user} ,{self.saturday_second_user}
                   created_at: {self.created_at.strftime("%d/%m/%Y , %H:%M:%S")}
                   updated_at: {self.updated_at.strftime("%d/%m/%Y , %H:%M:%S")}
                                                                               """
