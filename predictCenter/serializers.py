__author__ = 'tyan'
from django.forms import widgets
from rest_framework import serializers
from predictCenter.models import *

class HotStockSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    stockShortName = serializers.CharField(max_length=50)
    description = serializers.CharField(style={'type': 'textarea'})

    def create(self, validated_data):
        return HotStock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.stockShortName = validated_data.get('stockShortName', instance.stockShortName)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    class Meta:
        model = HotStock
        fields = ('id', 'stockShortName', 'description', 'created')

class StockSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    stockName = serializers.CharField(max_length=100)
    stockShortName = serializers.CharField(max_length=50)
    stockCode = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return Stock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.stockName = validated_data.get('stockName', instance.stockName)
        instance.stockShortName = validated_data.get('stockShortName', instance.stockShortName)
        instance.stockCode = validated_data.get('stockCode', instance.stockCode)
        instance.save()
        return instance

    class Meta:
        model = Stock
        fields = ('id', 'stockName', 'stockShortName', 'stockCode', 'created')

class UserStockSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    userId = serializers.IntegerField()
    stockShortName = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return UserStock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.stockShortName = validated_data.get('stockShortName', instance.stockShortName)
        instance.save()
        return instance

    class Meta:
        model = Stock
        fields = ('id', 'userId', 'stockShortName', 'created')

class StockPredictionSerializer(serializers.ModelSerializer):
    stockShortName = serializers.CharField(max_length=50)
    predict = serializers.FloatField()
    predictExpTime = serializers.IntegerField()

    def create(self, validated_data):
        return StockPrediction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('stockShortName', instance.stockShortName)
        instance.stockShortName = validated_data.get('predict', instance.predict)
        instance.predictExpTime = validated_data.get('predictExpTime', instance.predictExpTime)
        instance.save()
        return instance

    class Meta:
        model = Stock
        fields = ('id', 'stockShortName', 'predict', 'predictExpTime', 'created')

class HotStockInfoSerializer(serializers.Serializer):
    stockShortName = serializers.CharField(max_length=50)
    predict = serializers.FloatField()
    predictExpTime = serializers.IntegerField()
    created = serializers.DateTimeField()

