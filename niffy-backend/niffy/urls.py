from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

from niffy.views import home, invoice_create, do_notification, download, invoice

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'^invoices/(?P<id>[0-9]+)/download$', download, name='download'),
    url(r'^invoices/(?P<id>[0-9]+)$', invoice, name='invoice'),
    url(r'^invoices$', invoice_create, name='invoice_create'),
    url(r'^notification$', do_notification, name='do_notification'),

    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^csp/', include('cspreports.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=serve, show_indexes=True)
