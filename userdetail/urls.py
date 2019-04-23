from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^tables_object/$', views.index, name='index'),
    url(r'^userdetail/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^userdetail/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^userdetail/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^userdetail/create$', views.create, name='create'),
]
