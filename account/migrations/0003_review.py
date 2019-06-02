# Generated by Django 2.1 on 2019-06-01 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0004_auto_20190601_1449'),
        ('account', '0002_auto_20190601_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('point', models.IntegerField(blank=True, null=True)),
                ('hidden', models.BooleanField(default=False)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='center.Center')),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.Membership')),
            ],
        ),
    ]