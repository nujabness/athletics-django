from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="athletes"),
    url(r'^create', views.create),
    url(r'^update/(?P<id>[0-9]+)$', views.update),
    url(r'^operations$', views.operations),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete),

]
