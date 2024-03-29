# Generated by Django 4.0.6 on 2023-02-22 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default='', max_length=256)),
                ('email', models.CharField(blank=True, max_length=256)),
                ('postcode', models.CharField(blank=True, default='', max_length=256)),
                ('house_number', models.CharField(blank=True, default='', max_length=256)),
                ('phone_number', models.CharField(blank=True, default='', max_length=256)),
                ('street_name', models.CharField(blank=True, default='', max_length=256)),
                ('city', models.CharField(blank=True, default='', max_length=256)),
                ('country', models.CharField(blank=True, default='', max_length=256)),
                ('town', models.CharField(blank=True, default='', max_length=256)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
