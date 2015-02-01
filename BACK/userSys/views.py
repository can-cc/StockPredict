from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *
from rest_framework import permissions
from userSys.permissions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile


#!!!warning: Do not use this, ban all operations
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#!!!warning: Do not use this, ban all operations
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserInfoDetail(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, format=None):
        user = request.user
        userProfile = UserProfile.objects.get(user=user)
        serializer = UserInfoSerializer(userProfile)
        return Response(serializer.data)



class Alive(APIView):
    def get(self, request, format=None):
        if request.user.id != None:
            return Response(request.user.id)
        else:
            return Response(0)