from django.db import models


class TimeStamp(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CenterCategory(TimeStamp):
    name = models.CharField(max_length=64)


class Center(TimeStamp):
    name = models.CharField(max_length=128, null=False, blank=False)
    category = models.ForeignKey(CenterCategory,
                                 on_delete=models.PROTECT)
    phone = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=128, null=False, blank=False)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=True, default=True)
    description = models.TextField(null=True, blank=True)


class Program(TimeStamp):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    quota = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    available = models.BooleanField(null=False, blank=False, default=True)
    program_schedule = models.CharField(max_length=256)
    description = models.TextField()
    is_active = models.BooleanField(null=False, blank=False, default=True)
