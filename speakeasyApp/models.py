from django.db import models
from django.contrib.auth.models import  AbstractUser, User

#from fileservice.formatChecker import ContentTypeRestrictedFileField

import os
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here

class CustomUser(AbstractUser):
    email = models.EmailField("email", max_length=30,null=False, unique = True, )
    date_subscribed = models.DateField("date subscribed", null=True, auto_now_add=False)
    is_subscription_active = models.BooleanField("subscription_status" , default=False)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)
    subscription_type = models.CharField(max_length=255,null=True )
    pin = models.CharField("pin", null=False, max_length=6)

class Video(models.Model):
    id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    video = models.FileField()
    date_posted = models.DateTimeField("date posted", null=True, auto_now_add=True)


    


    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title


    def delete_completely(self, request, queryset):
        for filemodel in queryset:
            s3.delete_object(Bucket=BUCKET_NAME, Key=str(filemodel.file))
            filemodel.delete()

        delete_completely.short_description = 'Delete pointer and real file together'




class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content= models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    date_posted = models.DateTimeField("date posted", null=True, auto_now_add=True)

