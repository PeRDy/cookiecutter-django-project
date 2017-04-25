# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name='home'),
    url(r'^health_check/', include('health_check.urls')),
    url(r'^admin/', admin.site.urls),
]
