# Generated by Django 3.2.9 on 2021-11-30 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0005_auto_20211130_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='hospital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='memorials.hospital'),
        ),
    ]
