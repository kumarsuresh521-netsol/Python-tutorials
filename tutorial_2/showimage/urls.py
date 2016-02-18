from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ShowImageList.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.ShowImageDetail.as_view(), name='detail'),
]