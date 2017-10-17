from django.conf.urls import include,url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

#from mysite.core import views as core_views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'chat_app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^chat/([0-9]*)',views.chat_box,name='chat_box'),
    url(r'^messages/',views.MessageList.as_view())

]
