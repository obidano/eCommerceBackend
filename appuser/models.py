from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255, unique=True, null=True)
    phone = models.CharField(max_length=20)

    USERNAME_FIELD = 'name'

    class Meta:
        db_table = 'tb_user'
