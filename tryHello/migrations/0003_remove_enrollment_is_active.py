# Generated by Django 5.1.1 on 2024-10-04 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tryHello', '0002_enrollment_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='is_active',
        ),
    ]