from django.conf.urls import url

from . import views

app_name = 'courseBuddy'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/$', views.details, name='details'),
    url(r'^peoples/$', views.peoples_list, name='peoples'),
    url(r'^form/$', views.form, name='form'),
    url(r'^data/$', views.data, name='data'),
]