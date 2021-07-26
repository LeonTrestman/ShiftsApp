from datetime import timedelta
from .consts import DAYS_OF_WEEK, SHIFTS_HOURS_REG, SHIFTS_HOURS_REG_UNDERSCORE, SHIFTS_HOURS_WEEKENDS, SHIFTS_HOURS_WEEKENDS_UNDERSCORE,TYPE_OF_SHIFTS,MIN_VAL_SHIFT,MAX_VAL_SHIFT,SUBMIT_CHOICES 
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
                    f'{day}_{shift_type} = models.IntegerField(verbose_name =f"{day} {shift_type} {shift_hour}" ,default=0, choices=SUBMIT_CHOICES ,validators=[MinValueValidator(MIN_VAL_SHIFT),MaxValueValidator(MAX_VAL_SHIFT)])'
                )
                
        else:
            for shift_type,shift_hour in zip(TYPE_OF_SHIFTS,SHIFTS_HOURS_REG ) :

                exec(
                    f'{day}_{shift_type} = models.IntegerField(verbose_name =f"{day} {shift_type} {shift_hour}" ,default=0 , choices=SUBMIT_CHOICES ,validators=[MinValueValidator(MIN_VAL_SHIFT),MaxValueValidator(MAX_VAL_SHIFT)])'
                )    
         

            

    # datefields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"""name: {self.user_name} 
                   sunday: {self.sunday_evening} ,{self.sunday_night}
                   monday: {self.monday_evening} ,{self.monday_night}
                   tuesday: {self.tuesday_evening} ,{self.tuesday_night}
                   wednesday: {self.wednesday_evening} ,{self.thursday_night}
                   thursday: {self. friday_evening} ,{self. friday_night}
                   saturday: {self.saturday_evening} ,{self.saturday_night}
                   created_at: {self.created_at.strftime("%d/%m/%Y , %H:%M:%S")}
                   updated_at: {self.updated_at.strftime("%d/%m/%Y , %H:%M:%S")}
                                                                             """

    #returns the date of dayindex in the following week of the creation of the model
    #0 for the following sunday up to 6 for saturday
    def day_date(self,dayindex):
        day = self.created_at.replace(hour=0, minute=0, second=0, microsecond=0) #get created date and reset time
        ## get the date of the following day index of the creation date
        day-= timedelta(days=(day.weekday() + 1) % 7) # for a week that starts on a Sunday
        day +=timedelta(days=7+dayindex )  #adding the following week with dayindex
        return day


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
                   sunday: {self.sunday_evening_user} ,{self.sunday_night_user} 
                   monday: {self.monday_evening_user} ,{self.monday_night_user} 
                   tuesday: {self.tuesday_evening_user} ,{self.tuesday_night_user} 
                   wednesday: {self.wednesday_evening_user} ,{self.thursday_night_user}
                   thursday: {self. friday_evening_user} ,{self. friday_night_user}
                   saturday: {self.saturday_evening_user} ,{self.saturday_night_user}
                   created_at: {self.created_at.strftime("%d/%m/%Y , %H:%M:%S")}
                   updated_at: {self.updated_at.strftime("%d/%m/%Y , %H:%M:%S")}
                                                                               """
