# Generated by Django 2.2.3 on 2021-05-27 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakeasyApp', '0005_auto_20210527_2159'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Myvideo',
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'video', 'verbose_name_plural': 'videos'},
        ),
    ]
