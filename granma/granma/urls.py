from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'photoshare.views.home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^login$', 'photoshare.views.login', name='login'),
    url(r'^create_account$', 'photoshare.views.create_account', name='create_account'),

    url(r'^admin/', include(admin.site.urls)),
)