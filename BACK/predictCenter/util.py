__author__ = 'tyan'
import os
import re
from django.utils import timezone
import logging
logger = logging.getLogger('django')


def shortNameValid(symbol):
    if symbol == 'TestErr':
        return False
    return True

def recordStock(shortName):
    pass


def getNYSEToday():
    today = str(timezone.now().date())
    expStr = os.popen('Rscript Rscript/getNYSEToday.R ' + today).read()
    i = expStr.index('\n')
    date = expStr[i+1:i+11]
    verification = re.match(r'\d{4}-\d{2}-\d{2}', date)
    if verification is None:
        logger.error('Get getNYSEToday Error!')
        return False
    if date == today:
        return True
    else:
        return False

def getAdjClose(symbol):
    today = str(timezone.now().date())
    expStr = os.popen('Rscript Rscript/getNYSEToday.R ' + symbol + ' ' + today).read()
    i = expStr.rindex(' ')
    AdjClose = expStr[i+1: -1]
    verification = re.match(r'^(-?\d+)(\.\d+)?$', AdjClose)
    if verification is None:
        logger.error('Get getAdjClose Error!')
        raise Exception
    else:
        return AdjClose