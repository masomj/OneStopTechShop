# Generated by Django 4.0.6 on 2023-01-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=11),
        ),
    ]
