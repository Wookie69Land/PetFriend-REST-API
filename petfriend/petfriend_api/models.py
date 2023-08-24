from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

from .choices import *


class PetFriendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PetFriendUser.objects.create(user=instance)
    instance.petfrienduser.save()


def pet_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / pet_<id>/<filename>
    return 'pet_{0}/{1}'.format(instance.user.id, filename)


class Pet(models.Model):
    name = models.CharField(max_length=128, unique=True)
    genre = models.SmallIntegerField(choices=((1, "boy"), (2, "girl")))
    species = models.SmallIntegerField(choices=SPECIES)
    variety = models.CharField(max_length=128, null=True)
    birth_date = models.DateField(null=True, default=date.today)
    profile_image = models.ImageField(null=True, blank=True, upload_to=pet_directory_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(PetFriendUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - \
              ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age


class PetHealth(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=128)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    recovered = models.BooleanField(default=False)

