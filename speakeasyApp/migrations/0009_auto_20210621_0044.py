# Generated by Django 2.2.3 on 2021-06-20 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakeasyApp', '0008_newsletter_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter_users',
            name='email',
            field=models.EmailField(max_length=30, unique=True, verbose_name='email'),
        ),
    ]