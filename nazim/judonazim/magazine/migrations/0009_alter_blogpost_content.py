# Generated by Django 3.2.8 on 2021-12-14 07:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0008_alter_blogpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
