from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.loginPage, name="home"),
    url(r'login/$', views.loginPage, name="login"),
    url(r'register/$', views.registerPage, name="register"),
    url(r'logout/$', views.logoutUser, name="logout")
]