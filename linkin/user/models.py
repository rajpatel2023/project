from django.db import models
from django.db import models
from django.contrib.auth.models import User


from .choice import profation_choice, marrried_status_choice


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    phonenumber = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to="profile/", null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    hobbies = models.CharField(max_length=100, null=True, blank=True)
    profation = models.CharField(
        max_length=100, choices=profation_choice, null=True, blank=True
    )
    marrid_status = models.CharField(
        max_length=100,
        choices=marrried_status_choice,
        null=True,
        blank=True,
    )
    cast = models.CharField(max_length=100, null=True, blank=True)
    subcast = models.CharField(max_length=100, null=True, blank=True)
