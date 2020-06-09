from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^epreuves/', include('epreuves.urls')),
    url(r'^athletes/', include('athletes.urls')),
    url(r'^nationalites/', include('nationalites.urls')),
    url(r'^medailles/', include('medailles.urls')),
    url(r'^participations/', include('participations.urls'))
]