from django.db import models
from accounts.models import User


class Benefactor(models.Model):

    id = models.AutoField(primary_key= True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    experienceChoices = ((0, 'beginner'),
                         (1, 'intermediate'),
                         (2, 'expert'))
    experience= models.SmallIntegerField(choices=experienceChoices, default=0)

    free_Time_per_week= models.PositiveSmallIntegerField(default=0)