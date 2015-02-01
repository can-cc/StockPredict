from django.conf.urls import patterns, include, url
from django.contrib import admin
import predictCenter.views as PCviews
import userSys.views as USviews
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

#predictCenter
urlpatterns += [
    url(r'^hotStock/$', PCviews.HotStockList.as_view()),
    url(r'^hotStock/(?P<pk>[0-9]+)$', PCviews.HotStockDetail.as_view()),
    url(r'^hotStockInfo/$', PCviews.HotStockInfo.as_view()),


    url(r'^stock/$', PCviews.StockList.as_view()),
    url(r'^stock/(?P<pk>[0-9]+)$', PCviews.StockDetail.as_view()),

    url(r'^userStock/$', PCviews.UserStockList.as_view()),
    url(r'^userStock/(?P<pk>[0-9]+)$', PCviews.UserStockDetail.as_view()),

    url(r'^stockPrediction/$', PCviews.StockPredictionList.as_view()),
    url(r'^stockPrediction/(?P<symbol>[a-zA-Z]+)$', PCviews.StockPredictionDetail.as_view()),

    url(r'^spstat/$', PCviews.StockPredictionStatisticsList.as_view()),
    url(r'^spstat/(?P<pk>[0-9]+)$', PCviews.StockPredictionStatisticsDetail.as_view()),
]

#userSys
urlpatterns += [
    url(r'^userInfo/$', USviews.UserInfoDetail.as_view()),

    url(r'^alive/$', USviews.Alive.as_view()),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)