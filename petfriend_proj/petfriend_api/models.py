from django.db import models
from django.contrib.auth.models import User

from datetime import date

from .choices import *


class PetFriendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Pet(models.Model):
    name = models.CharField(max_length=128, unique=True)
    genre = models.SmallIntegerField(choices=((1, "boy"), (2, "girl")))
    species = models.SmallIntegerField(choices=SPECIES)
    variety = models.CharField(max_length=128, null=True)
    birth_date = models.DateField(null=True)
    user = models.ForeignKey(PetFriendUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - \
              ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

