__author__ = 'tyan'
from django.forms import widgets
from rest_framework import serializers
from predictCenter.models import *

class StockSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    stockName = serializers.CharField(max_length=100)
    symbol = serializers.CharField(max_length=50)
    sector = serializers.CharField(max_length=50)
    SE = serializers.CharField(max_length=20)
    industry = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Stock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.stockName = validated_data.get('stockName', instance.stockName)
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.stockCode = validated_data.get('stockCode', instance.stockCode)
        instance.save()
        return instance

    class Meta:
        model = Stock
        fields = ('id', 'stockName', 'symbol', 'sector', 'SE', 'industry')

class HotStockSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    stock = StockSerializer()
    description = serializers.CharField(style={'type': 'textarea'})
    status = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return HotStock.objects.create(**validated_data)

    class Meta:
        model = HotStock
        fields = ('id', 'stock', 'description', 'created', 'status')

class StockPredictionSerializer(serializers.ModelSerializer):
    stock = StockSerializer()
    predict = serializers.FloatField()
    predictRst = serializers.IntegerField()
    predictExpTime = serializers.IntegerField()

    def create(self, validated_data):
        return StockPrediction.objects.create(**validated_data)

    class Meta:
        model = Stock
        fields = ('id', 'stock', 'predict', 'predictExpTime', 'predictRst', 'created')

class UserStockSerializer(serializers.ModelSerializer):
    stock = StockSerializer()
    class Meta:
        model = UserStock
        fields = ('user', 'stock')

class StockPredictionStatisticsSerializer(serializers.ModelSerializer):
    stock = StockSerializer()
    class Meta:
        model = StockPrediction
        fields = ('stock', 'predict', 'adjClose', 'predictRst', 'predictExpTime', 'predictRst',
                    'timeOutAdjClose', 'earnings')