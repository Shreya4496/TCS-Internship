"""TCSProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ComplaintsForum.views import complaint_new
from Services.views import sla_new,service_new,service_create,service_all
from ChatBox.views import Login,Logout,Home,Post,Messages,register,privacy,activate,choosen_role
from Dashboard.views import Dashboard, post_list,pdf_view, DashboardCust, service_list, my_service_client
from homepage.views import HomePage
# from rest_framework import routers
from Dashboard import views
# from rest_framework.urlpatterns import format_suffix_patterns
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth.views import logout, login, password_reset, password_reset_done,password_reset_confirm,password_reset_complete

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^complaint_new/$', complaint_new, name='complaint_new'),
    url(r'^sla_new/$', sla_new, name='sla_new'),
    url(r'^login/$', Login, name='login'),
    url(r'^logout/$', Logout, name='logout'),
    url(r'^home/$', Home, name='home'),
    url(r'^post/$', Post, name='post'),
    url(r'^privacysettings/$', privacy, name='privacy'),
    url(r'^messages/$',Messages, name='messages'),
    url(r'^register/$', register , name='register'),
    url(r'^service_new/$', service_new , name='service_new'),
    url(r'^dashboard/$', Dashboard, name='dashboard'),
    url(r'^dashboardCust/$', DashboardCust, name='dashboardCust'),
    url(r'^pdf_view/$', pdf_view, name='pdf_view'),
    url(r'^homepage/$', HomePage, name='homepage'),
    url(r'^dashboard_new/',include('Dashboard.urls'), name='dashboard_api'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^spare/$', spare.html),
    # url(r'^spare/$', chart, name='chart'),
    url(r'^register_activate/activation/$',activate, name='activation'),
    url(r'^todo/$', TemplateView.as_view(template_name='todo.html'), name='todo'),
    url(r'^spare/$', post_list, name='spare'),
    url(r'^spare_list/$', service_list, name='provider'),
    url(r'^spare1/$', my_service_client, name='client'),
    url(r'^service_create/$', service_create, name='service_create'),
    url(r'^service_all/$', service_all, name='service_all'),

    url(r'^reset-password/$',password_reset, name='reset_password'),
    url(r'^reset-password/done/$',password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete,name='password_reset_complete')
    # url(r'^spare/$', Dashboard.views.json_search, name="search")
]

# urlpatterns = format_suffix_patterns(urlpatterns)
