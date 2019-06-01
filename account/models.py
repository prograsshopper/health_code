from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    center = models.ForeignKey('center.Center', on_delete=models.PROTECT,
                               null=True, blank=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    nick_name = models.CharField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=40, null=True, blank=True)
    is_partner = models.BooleanField(default=False, null=False, blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)


class Review(models.Model):
    center = models.ForeignKey('center.Center', on_delete=models.PROTECT, null=False, blank=False)
    membership = models.ForeignKey('center.Membership', on_delete=models.CASCADE,
                                   null=False, blank=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    point = models.IntegerField(blank=True, null=True)
    hidden = models.BooleanField(default=False, null=False, blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)