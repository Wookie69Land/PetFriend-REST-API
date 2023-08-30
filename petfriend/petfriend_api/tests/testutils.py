from random import sample, randint, choice
from faker import Faker, Factory

import random

from petfriend_api.models import *
from petfriend_api.choices import *

faker = Faker("en")
fake = Factory.create("en")

def random_user():
    users = User.objects.all()
    return choice(users)


def create_name():
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = first_name + last_name + str(random.randint(1, 666))
    return username


def create_user():
    username = create_name()
    email = fake.email()
    password = "FakeFake1234@"
    person = User.objects.create_user(username=username,
                                      email=email,
                                      password=password)
    return person


def create_petfrienduser():
    person = create_user()
    person.petfrienduser.phone = fake.phone_number()
    return person