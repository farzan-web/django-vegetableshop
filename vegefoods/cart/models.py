from django.db import models
from django.contrib.auth.models import User
from shop.models import Vegtables
# Create your models here.

class Wishlist(models.Model):
    user = models.ForeignKey(User, related_name="user",on_delete=models.CASCADE)
    vegtable = models.ForeignKey(Vegtables,related_name='vegtable',on_delete=models.CASCADE)
    wish = models.BooleanField()

    def __str__(self):
        temp_str = self.user.__str__() + " / " + self.vegtable.__str__()
        return temp_str

    class Meta:
        ordering = ["user"]