from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^cms/$', views.CmsList.as_view()),
    url(r'^cms/(?P<pk>[0-9]+)/$', views.CmsDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)