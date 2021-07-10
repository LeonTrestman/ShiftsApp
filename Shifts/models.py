from .consts import DAYS_OF_WEEK,TYPE_OF_SHIFTS
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# model for user availability for shifts
# this model has 2 shifts for each day in a week


class shiftSubmitTwo(models.Model):
    # values for availability
    min_val_shift = 0
    max_val_shift = 3

    # on deletetion of user his shifts should remain in the database
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="shift_submitter",
        on_delete=models.DO_NOTHING,
    )

    # creating the integerfield of availability of the shifts form user
    for day in DAYS_OF_WEEK:
        for shift_type in TYPE_OF_SHIFTS:
            exec(
                f"{day}_{shift_type} = models.IntegerField(default=0,validators=[MinValueValidator(min_val_shift),MaxValueValidator(max_val_shift)])"
            )

    # datefields
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
