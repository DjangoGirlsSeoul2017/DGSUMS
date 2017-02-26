from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/login/$', login,
        {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('users.urls')),
    url(r'^', include('events.urls')),
    url(r'^', include('social_django.urls', namespace='social')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]