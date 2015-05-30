from django.db import models
from django.contrib.auth.models import User

# Question
class Question(models.Model):
    question = models.CharField(max_length=200)


# Answer choice for a question
# Each choice also has some points
class Choice(models.Model):
    choice = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    question = models.ForeignKey(Question)


# Victim, can be Expected or Real Victim
# Also stores location (lat, long) of victim, victim's answers 
# to the questions and user who submitted the form for the victim
class Victim(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    VICTIM_TYPES = (
        (1, 'Victim'),
        (2, 'Expected Victim'),
    )
    victim_type = models.IntegerField(choices=VICTIM_TYPES)
    choices = models.ManyToManyField(Choice, blank=True)
    user = models.ForeignKey(User)


# Extra information of the user that is not stored by django by default
class UserExtra(models.Model):
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    user = models.OneToOneField(User)

