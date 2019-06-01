from django.db import models


class CenterCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    @staticmethod
    def initial_migrate():
        categories = ['수영', '필라테스', '헬스', 'PT', '크로스핏', '요가',
                      '에어로빅']
        for c in categories:
            CenterCategory.objects.create(name=c)


class Center(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    category = models.ForeignKey(CenterCategory,
                                 on_delete=models.PROTECT)
    phone = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=128, null=False, blank=False)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=True, default=True)
    description = models.TextField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)


class Program(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    quota = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    available = models.BooleanField(null=False, blank=False, default=True)
    program_schedule = models.CharField(max_length=256)
    description = models.TextField()
    is_active = models.BooleanField(null=False, blank=False, default=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)


class Membership(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.PROTECT)
    center = models.ForeignKey('center.Center', on_delete=models.PROTECT)
    program = models.ForeignKey('center.Program', on_delete=models.PROTECT)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
