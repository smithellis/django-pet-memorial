# Generated by Django 3.2.9 on 2021-11-29 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0002_alter_customuser_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorial',
            name='memorial_create_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donation_date', models.DateField(auto_now=True)),
                ('donation_status', models.CharField(max_length=200)),
                ('donation_code', models.CharField(max_length=200)),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memorials.fund')),
                ('memorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memorials.memorial')),
            ],
        ),
    ]
