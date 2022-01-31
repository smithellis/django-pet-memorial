# Generated by Django 3.2.9 on 2021-11-30 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0004_auto_20211130_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorial',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_code',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
