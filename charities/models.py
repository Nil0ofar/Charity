from django.db import models
from accounts.models import User


class Benefactor(models.Model):

    id = models.AutoField(primary_key= True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    experienceChoices = ((0, 'beginner'),
                         (1, 'intermediate'),
                         (2, 'expert'))
    experience= models.SmallIntegerField(choices=experienceChoices, default=0)

    free_time_per_week= models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):

    id = models.AutoField(primary_key = True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    reg_number = models.CharField(max_length=10)


class Task(models.Model):
    id = models.AutoField(primary_key=True)

    assigned_benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.SET_NULL)

    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)

    age_limit_from = models.IntegerField(blank=True, null=True)

    age_limit_to = models.IntegerField(blank=True, null=True)

    date = models.DateField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    genderLimitChoices = (('F', 'Female'),
                          ('M', 'Male'))
    gender_limit = models.CharField(max_length=1, choices=genderLimitChoices, blank=True, null=True)

    stateChoices = (('P', 'Pending'),
                    ('W', 'Waiting'),
                    ('A', 'Assigned'),
                    ('D', 'Done'))
    state = models.CharField(max_length=1, choices=stateChoices, default='P')

    title = models.CharField(max_length=100)