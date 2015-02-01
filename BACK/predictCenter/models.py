from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    stockName = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50, unique=True, db_index=True, db_tablespace="indexes")
    IPOyear = models.CharField(null=True, blank=True, max_length=20)
    sector = models.CharField(null=True, blank=True, max_length=100)
    industry = models.CharField(null=True, blank=True, max_length=100)
    SE = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

# predictRst
# 0 not check
# 1 Correct
# -1 Error
class StockPrediction(models.Model):
    created = models.DateField(auto_now_add=True)
    stock = models.ForeignKey(Stock, related_name='prediction')
    predict = models.FloatField(default='0.0')
    predictRst = models.IntegerField(blank=True, null=True)
    predictExpTime = models.IntegerField()
    adjClose = models.FloatField()
    timeOutAdjClose = models.FloatField(blank=True, null=True)
    earnings = models.FloatField(blank=True, null=True)
    class Meta:
        ordering = ('-created',)

class StockData(models.Model):
    stock = models.ForeignKey(Stock, related_name='data')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class HotStock(models.Model):
    stock = models.ForeignKey(Stock)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('created', 'status')

class UserStock(models.Model):
    user = models.ForeignKey(User, related_name='stock')
    stock = models.ForeignKey(Stock)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class PreJudgeStock(models.Model):
    stockPrediction = models.ForeignKey(StockPrediction, related_name='preJudge')
    created = models.DateField(auto_now_add=True)
    judgeDay = models.DateField()
    dtl = models.IntegerField()