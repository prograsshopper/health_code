# Generated by Django 2.1 on 2019-06-02 00:37

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0006_auto_20190602_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='main_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='center/center/%Y/%M/%D'),
        ),
    ]
