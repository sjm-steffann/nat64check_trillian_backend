"""trillian_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#  Copyright (c) 2018, S.J.M. Steffann. This software is licensed under the BSD
#  3-Clause License. Please see the LICENSE file in the project root directory.
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from generic.urls import generic_router
from generic.views import reload_uwsgi
from instances.urls import instances_router
from measurements.urls import measurements_router

router = DefaultRouter()
router.registry.extend(generic_router.registry)
router.registry.extend(instances_router.registry)
router.registry.extend(measurements_router.registry)

# TODO: Consider OTP for Admin site
# otp_admin_site = OTPAdminSite(OTPAdminSite.name)
# for model_cls, model_admin in admin.site._registry.items():
#     otp_admin_site.register(model_cls, model_admin.__class__)

urlpatterns = [
    url(r'^swagger/$', get_swagger_view(title='NAT64Check Trillian API')),
    url(r'^docs/', include_docs_urls(title='NAT64Check Trillian API')),

    url(r'^admin/reload/$', reload_uwsgi, name='reload_uwsgi'),

    # TODO: Consider OTP for Admin site
    # url(r'^admin/', otp_admin_site.urls),

    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/$', RedirectView.as_view(url='v1/')),
    url(r'^api/v1/', include((router.urls, 'api'), namespace='v1')),

    url(r'^$', RedirectView.as_view(url='api/')),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns = urlpatterns + [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
