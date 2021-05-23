from django.db import models
from django.contrib.auth.models import  AbstractUser




# Create your models here

class CustomUser(AbstractUser):
    #username= None
    email = models.EmailField("email", max_length=30,null=False, unique = True, )
    date_subscribed = models.DateField("date subscribed", null=True, auto_now_add=False)
    is_subscription_active = models.BooleanField("subscription_status" , default=False)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)
    pin = models.CharField("pin", null=False, max_length=6)
    


class Video(models.Model):
    id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    video = models.FileField(upload_to='media/')
    date_posted = models.DateTimeField("date posted", null=True, auto_now_add=True)



    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title




class Article(models.Model):
    id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content= models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    date_posted = models.DateTimeField("date posted", null=True, auto_now_add=True)
    

