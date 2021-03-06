# Generated by Django 3.2.8 on 2021-12-10 21:43

import ckeditor.fields
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
            name='Moderators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='regUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nickname', models.CharField(max_length=50)),
                ('userstatus', models.CharField(choices=[('active', 'פעיל'), ('banned', 'הושבת'), ('deleted', 'נמחק'), ('deactivate', 'לא פעיל')], default='active', max_length=10)),
                ('usrrole', models.CharField(choices=[('regular', ''), ('moderator', 'מודרטור'), ('admin', 'מנהל'), ('owner', 'מאסטר')], default='regular', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('subtitle', models.CharField(default='', max_length=200)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='')),
                ('author_email', models.EmailField(blank=True, default='ronnythenazi@gmail.com', max_length=254)),
                ('datepublished', models.DateField(auto_now_add=True)),
                ('datelastupdated', models.DateField(auto_now=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('publishstatus', models.CharField(choices=[('public', 'ציבורי'), ('private', 'פרטי')], default='private', max_length=10)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
