__author__ = 'tyan'
from rest_framework import serializers
from predictCenter.models import UserStock
from django.contrib.auth.models import User
from .models import UserProfile


class SysUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'date_joined', 'email')

    def create(self, validated_data):
        rawPassword = validated_data['password']
        validated_data['password'] = ""
        user = User.objects.create(**validated_data)
        user.set_password(rawPassword)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = instance.password
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.first_name)
        instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(many=True, queryset=UserStock.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')

class SysUserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'date_joined')

class UserInfoSerializer(serializers.ModelSerializer):
    user = SysUserSimpleSerializer()
    nickName = serializers.CharField()
    photo = serializers.ImageField(required=False)
    selfDescription = serializers.CharField(required=False)
    hometown = serializers.CharField(required=False)
    nowCity = serializers.CharField(required=False)

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #
        #
        #
        instance.save()
        return instance

    class Meta:
        model = UserProfile
        fields = ('user', 'nickName', 'photo', 'selfDescription', 'hometown', 'nowCity')
