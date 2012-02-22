from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fk.views.home', name='home'),
    # url(r'^fk/', include('fk.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
