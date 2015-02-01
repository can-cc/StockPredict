from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='UserProfile')
    nickName = models.CharField(max_length=30)
    photo = models.ImageField(blank=True, null=True)
    selfDescription = models.TextField(blank=True, null=True)
    hometown = models.CharField(max_length=30, blank=True, null=True)
    nowCity = models.CharField(max_length=30, blank=True, null=True)

class UserSetting(models.Model):
    user = models.ForeignKey(User, related_name='UserSetting')

class UserCount(models.Model):
    user = models.ForeignKey(User, related_name='UserCount')
    coin = models.IntegerField()#money
    total = models.IntegerField()#history money

class UserPredictPermission(models.Model):
    user = models.ForeignKey(User, related_name='UserPredictPermission')
    permissionLevel = models.IntegerField()
    permissionTime = models.IntegerField()

class RechargeRecord(models.Model):
    user = models.ForeignKey(User, related_name='RechargeRecord')
    coin = models.IntegerField()
    peyment = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)