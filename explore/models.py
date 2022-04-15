from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.

class Charity(AbstractBaseUser):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    charity_theme = models.CharField(max_length=250)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    pic_link = models.CharField(max_length=1000)
    charity_id = models.CharField(max_length=7, )
    certificate = models.ImageField(upload_to="media", blank=True)
    username = models.CharField(max_length=100,primary_key=True)
    identifier = models.CharField(max_length=40)
    USERNAME_FIELD = 'identifier'
    email = models.EmailField()
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.name + ' - ' + str(self.rating)

    def get_queryset(self):
        return Charity.objects.all().orderby('-rating')
