from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
app_name = 'courseBuddy'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/$', views.details, name='details'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', auth_views.login, name= 'login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^peoples/$', views.peoples_list, name='peoples'),
    url(r'^form/$', views.form, name='form'),
    url(r'^data/$', views.data, name='data'),
]