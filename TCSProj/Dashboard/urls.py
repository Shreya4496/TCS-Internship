from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from Dashboard import views

urlpatterns = [
    url(r'^api/$',views.ClientList.as_view(), name='api'),
    url(r'^api/(?P<pk>[0-9]+)/$', views.ClientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)