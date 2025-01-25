import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spamdetection.settings")
django.setup()
import random

from user.models import User
from contacts.models import Contact
from spam.models import SpamReport


def generate_random_phone():
    """Generates a random phone number"""
    return f'+91{random.randint(1000000000, 9999999999)}'

def generate_random_name():
    """Generates a random name"""
    names = ['Makima',"Denji","Levi","Mikasa","Luffy","Nayuta","Zoro","charlie","Nami","reze"]
    return f"{random.choice(names)}"

def generate_random_email( name,no_):
    """Generates a random email on user's name"""
    name_part = name.replace(' ', '').lower()
    return f"{name_part}{no_}@gmail.com"

def execute():
    # Create 10 random users
    users = []
    for _ in range(10):
        name = generate_random_name()
        phone = generate_random_phone()
        email = generate_random_email(name,phone[-4:])
        user = User.objects.create(
            username=phone,  # Using phone as username
            phone=phone,
            name=name,
            email=email,
        )
        users.append(user)

    # Create 30 random contacts
    for _ in range(30):
        while True:
            try:
                user = random.choice(users)  # Randomly choose a user for the contact
                contact_name = generate_random_name()
                contact_phone = generate_random_phone()
                Contact.objects.create(
                    phone=contact_phone,
                    user=user,
                    name=contact_name,
                )
                break
            except:
                "retrying as phone,user need to be unique"
                pass

    # Create 15 random spam reports
    for _ in range(15):
        user = random.choice(users)  # Randomly choose a user to report spam
        phone = generate_random_phone()  # Random phone number for spam report
        SpamReport.objects.create(
            phone=phone,
            spammed_by=user,
        )
execute()