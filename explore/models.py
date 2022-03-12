from django.db import models
from sqlalchemy import true

# Create your models here.

class Charity(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    charity_theme = models.CharField(max_length=250)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    pic_link = models.CharField(max_length=1000)
    charity_id = models.CharField(max_length=7, primary_key=true)

    def __str__(self) -> str:
        return self.name + ' - ' + str(self.rating)

    def get_queryset(self):
        return Charity.objects.all().orderby('-rating')

