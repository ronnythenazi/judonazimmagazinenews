# Generated by Django 3.2.8 on 2022-01-19 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0077_alter_notification_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
