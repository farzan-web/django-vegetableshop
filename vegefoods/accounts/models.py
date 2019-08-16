from django.db import models
from django.contrib.auth.models import User

COUNTRY_CHOICES = (
    ('france','France'),
    ('iran', 'Iran'),
    ('philippines','Philippines'),
    ('hongkong','Hongkong'),
    ('japan','Japan'),
    ('unitedkingdom','United kingdom'),
    ('unitedstates','United states'),
)
# Create your models here.
# class User(auth.models.User,auth.models.PermissionsMixin):
    
#     def __str__(self):
#         return "@{}".format(self.username)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    state_country = models.CharField(max_length=10, blank=False, choices=COUNTRY_CHOICES, default='france')
    address = models.TextField(blank=False, default='')
    phone_number = models.PositiveIntegerField(blank=False)
