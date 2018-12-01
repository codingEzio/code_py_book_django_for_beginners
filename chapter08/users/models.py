from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ About the params of 'age'
            null    db related
            blank	form related (validation)
    """

    age = models.PositiveIntegerField(null=True, blank=True)
