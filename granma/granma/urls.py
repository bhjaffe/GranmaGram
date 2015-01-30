from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'photoshare.views.home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    # url(r'^/complete/google-oauth2/', 'photoshare.views.home', name='home'),
    # url(r'^auth/google/', include('google_oauth.urls'))

    url(r'^admin/', include(admin.site.urls)),
)