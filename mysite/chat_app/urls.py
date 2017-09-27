from django.conf.urls import include,url
from . import views

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

#from mysite.core import views as core_views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'chat_app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^index/([0-9]*)',views.index,name='index'),
    url(r'^test', views.test, name='test'),
]
