from predictCenter.models import HotStock,Stock,UserStock
from predictCenter.serializers import *
from rest_framework import generics
from rest_framework import permissions
from userSys.permissions import IsOwnerOrReadOnly, IsSelf
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseBadRequest, Http404
from predictCenter.util import shortNameValid
from .permissions import IsAdminUserOrReadOnly
from django.utils import timezone
from .tasks import predict
import redis
import datetime
import logging
from django.core.cache import cache


logger = logging.getLogger('django')

class HotStockList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = HotStock.objects.all()
    serializer_class = HotStockSerializer

class HotStockDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = HotStock.objects.all()
    serializer_class = HotStockSerializer

class StockList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class UserStockList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        userStocks = UserStock.objects.filter(user=request.user)
        serializer = UserStockSerializer(userStocks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        symbol = request.data['symbol']
        if symbol is None:
            raise HttpResponseBadRequest
        try:
            stock = Stock.objects.get(symbol=symbol)
        except:
            raise Http404
        try:
            userStock = UserStock(user=request.user,
                                  stock=stock)
            userStock.save()
        except:
            return Response({'Error': 'UnKnown'})
        return Response({'Success': 'Success'})

class UserStockDetail(generics.RetrieveDestroyAPIView):
    queryset = UserStock.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsSelf)
    serializer_class = UserStockSerializer

class StockPredictionList(generics.ListCreateAPIView):
    queryset = StockPrediction.objects.all()
    serializer_class = StockPredictionSerializer

class StockPredictionDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, symbol, format=None):
        user = request.user
        logger.info(str(datetime.datetime.now()) + ' [' + symbol + '] request predict')
        if request.GET.get('expD') is not None:
            expD = request.GET.get('expD')
        else:
            expD = 10
        try:
            stock = Stock.objects.get(symbol=symbol)
        except:
            logger.info(str(datetime.datetime.now()) + ' [' + symbol + '] error input!')
            return Response({"Error": "Without this stock! Please check!"})  #Without this stock! Please check!
        try:
            if stock.SE is 'NYSE':
                now = timezone.now().date()
            else:
                now = datetime.datetime.now().date()
            querySet = stock.prediction.all()
            if len(querySet) == 0:
                if cache.get(symbol) == None or str(cache.get(symbol)) != str(expD):
                        logger.info(str(datetime.datetime.now()) + ' [' + symbol + '] prepare to predict')
                        cache.set(symbol, str(expD))
                        predict.delay(symbol, expD, user)
                else:
                    logger.info(str(datetime.datetime.now()) + ' [' + symbol + '] predict is alreadly in queue!')
                return Response({'Success': 'please wait!'})
            else:
                cacheP = stock.prediction.all()[0]
                if now == cacheP.created and str(expD) == str(cacheP.predictExpTime):
                    logger.info(str(datetime.datetime.now()) + ' [' + symbol + '] ' + str(expD) + ' day prediction in db!')
                    print cacheP
                    serializer = StockPredictionSerializer(cacheP)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    if cache.get(symbol) == None or str(cache.get(symbol)) != str(expD):
                        logger.info(str(datetime.datetime.now()) + ' ' + 'Prepare predict ' + symbol)
                        cache.set(symbol, str(expD))
                        predict.delay(symbol, expD, user)
                    else:
                        logger.info(str(datetime.datetime.now()) + ' [' + symbol + '] predict is alreadly in queue!')
                    return Response({'Success': 'please wait!'})
        except:
            logger.error(str(datetime.datetime.now()) + ' [' + symbol + '] predict control error!')
            return Response({"Error": "UnKnown!"})


class HotStockInfo(APIView):
    def get(self, request, format=None):
        rst = []
        hotstocks = HotStock.objects.all()
        for hotStock in hotstocks:
            stockPredictions = StockPrediction.objects.filter(stock=hotStock.stock)
            if len(stockPredictions) is not 0:
                rst.append(stockPredictions[0])
        serializer = StockPredictionSerializer(rst, many=True)
        return Response(serializer.data)

class StockPredictionStatisticsList(generics.ListCreateAPIView):
    queryset = StockPrediction.objects.all()
    serializer_class = StockPredictionStatisticsSerializer

class StockPredictionStatisticsDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = StockPrediction.objects.all()
    serializer_class = StockPredictionStatisticsSerializer