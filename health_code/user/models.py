from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email_id = models.EmailField(unique=True, max_length=75, default=None, null=True)  # Email Id
    center_id = models.ForeignKey('center.Center', db_column='center_id')
    name = models.CharField(max_length=30, default=None, null=True)
    nick_name = models.CharField(max_length=30, default=None, null=True)
    profile_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    phone = models.CharField(max_length=40, default=None, null=True)
    is_staff = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_Date = models.DateTimeField(auto_now=True)


class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', db_column='user_id')
    center_id = models.ForeignKey('center.Center', db_column='')
    program_id = models.ForeignKey('center.Program', db_column='')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)