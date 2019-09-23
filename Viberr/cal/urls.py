from django.conf.urls import url
from . import views

app_name = 'cal'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^bid/$', views.bid, name='bid'),
    url(r'^calenders/$', views.calenders, name='calenders'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^testing2/$', views.testing, name='testing'),
    url(r'^spot_list/(?P<website>[\w-]+)$', views.spot_list, name='spot_list'),
    url(r'^advertise/$', views.advertise, name='advertise'),
]