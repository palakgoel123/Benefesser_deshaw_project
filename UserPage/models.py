from django.db import models

# Create your models here.
from django.contrib.auth.models import User,AnonymousUser


class balance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    balance = models.IntegerField(default = 0)