from django.db import models

# Create your models here.
class StockPrediction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    stockShortName = models.CharField(max_length=100)
    predict = models.CharField(max_length=20, default='unknown')
    predictExpTime = models.IntegerField()

    class Meta:
        ordering = ('created',)
#
# class HotStockPrediction(models.Model):
#     stockName = models.CharField(max_length=100)
#     stockShortName = models.CharField(max_length=50)
#     stockCode = models.IntegerField(max_length=25)
#     prediction = models.CharField(max_length=10)
#     Tvalue = models.FloatField(max_length=20)
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ('created',)

class Stock(models.Model):
    stockName = models.CharField(max_length=100)
    stockShortName = models.CharField(max_length=50, unique=True)
    stockCode = models.IntegerField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class HotStock(models.Model):
    stockShortName = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('created',)

class UserStock(models.Model):
    userId = models.IntegerField()
    stockShortName = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class HotStockInfo(object):
    def __init__(self,stockShortName,predict,predictExpTime,created):
        self.stockShortName = stockShortName;
        self.predict = predict;
        self.predictExpTime = predictExpTime;
        self.created = created;
