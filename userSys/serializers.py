__author__ = 'tyan'
from django.contrib.auth.models import User
from rest_framework import serializers
from predictCenter.models import UserStock

class UserSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(many=True, queryset=UserStock.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'date_joined')