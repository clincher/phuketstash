""" Default urlconf for stash """

from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = i18n_patterns('',
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('game.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^bad/$', bad),
    url(r'', include('social_auth.urls')),
    url(r'^', include('cms.urls')),
    url(r'', include('base.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
