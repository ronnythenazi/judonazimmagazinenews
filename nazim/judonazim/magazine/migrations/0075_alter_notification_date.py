# Generated by Django 3.2.8 on 2022-01-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0074_alter_album_myfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]