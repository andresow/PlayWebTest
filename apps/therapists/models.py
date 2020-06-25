from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Therapist(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="therapist")
    typeIdentification = models.CharField(max_length=64, verbose_name='Tipo de identificación')
    identification = models.BigIntegerField()
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    genre = models.CharField(max_length=64, verbose_name='Género')
    typeUser = models.CharField(max_length=64, verbose_name='Tipo de usuario')

        # Options for types of id