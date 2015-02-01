__author__ = 'tyan'
from celery import task
import logging
logger = logging.getLogger(__name__)
import os
from .models import Stock, StockPrediction, PreJudgeStock
import logging
import datetime
import re
from django.core.cache import cache
logger = logging.getLogger('django')
from django.utils import timezone
from .util import getNYSEToday, getAdjClose

@task()
def add():
    x=1;y=2
    print x+y
    return x + y

@task()
def predict(symbol, expD, user):
    try:
        stock = Stock.objects.get(symbol=symbol)
        expStr = os.popen('Rscript Rscript/predict.R ' + symbol).read()
        cells = expStr.split(' ')

        logger.info(str(datetime.datetime.now()) + ' ' + symbol +
                     ' predict R output: ' + str(cells))

        # if len(cells) != 16:
        #     logger.error(str(datetime.datetime.now()) + ' ' + symbol + ' predict output Error!')
        #     raise Exception
        #     logger.warning(str(datetime.datetime.now()) + ' ' + symbol +
        #                    ' predict Error! and try to retry!')
        #     retryPredict(symbol, expD, 0, user)
        #     return
        predictT = cells[-2][:-4]
        adjClose = cells[-1][:-1]
        #Verify that float
        if re.match(r'^(-?\d+)(\.\d+)?$', predictT) is None:
            logger.error(str(datetime.datetime.now()) + ' ' + symbol + ' predictT format Error!')
            raise Exception
        #     logger.warning(str(datetime.datetime.now()) + ' ' + symbol +
        #                    ' predict Error! and try to retry!')
        #     retryPredict(symbol, expD, 0, user)
        #     return
        logger.info(str(datetime.datetime.now()) + ' ' + symbol + ' predict T = ' + predictT)
        predictT = float(predictT)
        stockP = StockPrediction(stock=stock,
                                 predict=predictT,
                                 predictRst=0,
                                 predictExpTime=expD,
                                 adjClose=adjClose)
        stockP.save()
        logger.info(str(datetime.datetime.now()) + ' ' + symbol + ' stockP save success!')

        now = timezone.now().date()
        midDay = datetime.timedelta(days=int(expD))
        judgeDay = now + midDay
        preJudge = PreJudgeStock(stockPrediction=stockP,
                                 judgeDay=judgeDay,
                                 dtl=expD)
        preJudge.save()
        logger.info(str(datetime.datetime.now()) + ' ' + symbol + ' preJudge save success!')

        cache.delete(symbol)
        logger.info(str(datetime.datetime.now()) + ' ' + symbol + ' predict success!')
    except:
        logger.error(str(datetime.datetime.now()) + ' ' + symbol + ' predict Error!')
        cache.delete(symbol)

#has bug: only retry one time
def retryPredict(symbol, expD, timeCount, user):
    if timeCount == 2:
        logger.error(str(datetime.datetime.now()) + ' ' + symbol +
                     'had retry predict ' + timeCount + ' times!But still wrong!')
        return
    logger.info(str(datetime.datetime.now()) + ' ' + symbol + ' retry predict at 1st time!')
    try:
        stock = Stock.objects.get(symbol=symbol)
        expStr = os.popen('Rscript Rscript/predict.R ' + symbol).read()
        i = expStr.rindex(' ')
        predictT = (expStr[i:-1])
        #Verify that float
        if re.match(r'^(-?\d+)(\.\d+)?$', predict) is None:
            logger.warning(str(datetime.datetime.now()) + ' ' + symbol +
                           str(timeCount) + 'time retry predict Error! and try to retry!')
            retryPredict(symbol, expD, timeCount+1, user)
            return
        stockP = StockPrediction(stock=stock,
                                 predict=predictT,
                                 predictRst=0,
                                 predictExpTime=expD)
        stockP.save()
        cache.delete(symbol)
        logger.info(str(datetime.datetime.now()) + ' ' + symbol + ' retry predict success!')
    except:
        logger.error(str(datetime.datetime.now()) + ' ' + symbol + ' retry predict Error!')

@task()
def judge(SE):
    if getNYSEToday:
        try:
            preUpdates = PreJudgeStock.objects.filter(dtl__gt=0, stockPrediction__stock__SE=SE)
            if len(preUpdates) is not 0:
                for preUpdate in preUpdates:
                    dtl = preUpdate.dtl - 1
                    preUpdate.update(dtl=dtl)
        except:
            logger.error('Judge update dtl Error!')
        try:
            preJudges = PreJudgeStock.objects.filter(dtl=0, stockPrediction__stock__SE=SE)
            if len(preUpdates) is not 0:
                try:
                    for preJudge in preJudges:
                        symbol = preJudge.stockPrediction.stock.symbol
                        adjClose = getAdjClose(symbol)
                        earnings = float(adjClose) - float(preJudge.stockPrediction.adjClose)
                        preJudge.update(stockPrediction__timeOutAdjClose=adjClose, earnings=earnings)
                except:
                    logger.error('Judge Judge Stock Update Error!')
        except:
            logger.error('Judge Judge Stock Error!')
    else:
        pass