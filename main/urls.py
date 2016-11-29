from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^data/$', views.data),
    url(r'^data/(?P<rtype>\w+)/$', views.data),
    url(r'^data/(?P<rtype>\w+)/(?P<value>\d+)$', views.data),
    url(r'^fieldreports$', views.field_reports_overview),
    url(r'^fieldreport/(?P<id>\d+)$', views.field_report)
]