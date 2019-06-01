from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    center = models.ForeignKey('center.Center', on_delete=models.PROTECT)
    name = models.CharField(max_length=30, null=False, blank=False)
    nick_name = models.CharField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=40, null=True, blank=True)
    is_partner = models.BooleanField(default=False, null=False, blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
