# Generated by Django 2.0.7 on 2021-09-28 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210928_1737'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
