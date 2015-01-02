from predictCenter.models import HotStock,Stock,UserStock
from predictCenter.serializers import *
from rest_framework import generics
from rest_framework import permissions
from userSys.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from predictCenter.util import shortNameValid
import os

class HotStockList(generics.ListCreateAPIView):
    queryset = HotStock.objects.all()
    serializer_class = HotStockSerializer

class HotStockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HotStock.objects.all()
    serializer_class = HotStockSerializer

class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class UserStockList(generics.ListCreateAPIView):
    queryset = UserStock.objects.all()
    serializer_class = UserStockSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        userStocks = UserStock.objects.all()
        serializer = UserStockSerializer(userStocks, many=True)
        return Response(serializer.data)


class UserStockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserStock.objects.all()
    serializer_class = UserStockSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class StockPredictionList(generics.ListCreateAPIView):
    queryset = StockPrediction.objects.all()
    serializer_class = StockPredictionSerializer

class StockPredictionDetail(APIView):

    def get(self, request, sName, format=None):
        if shortNameValid(sName):
            sn = len(StockPrediction.objects.filter(stockShortName=sName))
            if sn == 0:
                expStr = os.popen('Rscript Rscript/predict.R ' + sName).read()
                i = expStr.rindex(' ')
                expT = (expStr[i:-1])
                return Response(expT)
            else:
                sps = StockPrediction.objects.get(stockShortName=sName)
                serializer = StockPredictionSerializer(sps)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(0)#Without this stock! Please check!


class HotStockInfo(APIView):
    def get(self, request, format=None):
        rst = []
        hotstocks = HotStock.objects.all()
        for hotStock in hotstocks:
            stockPredictions = StockPrediction.objects.filter(stockShortName=hotStock.stockShortName)
            if stockPredictions.count() is not 0:
                stockPrediction = stockPredictions[0]
                created = stockPrediction.created
                predict = stockPrediction.predict
                predictExpTime = stockPrediction.predictExpTime
                stockShortName = stockPrediction.stockShortName
                hsi = HotStockInfo(stockShortName=stockShortName,predict=predict,predictExpTime=predictExpTime,created=created)
                rst.append(hsi)
        serializer = HotStockInfoSerializer(rst, many=True)
        return Response(serializer.data)

