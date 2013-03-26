from django.conf.urls.defaults import *
from django.conf import settings
from blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^articles/(?P<slug>[\w-]+)$', views.article, name='article'),
    url(r'^admin/articles/(?P<slug>[\w-]+)/edit$', views.article_edit, name='article_edit'),
    url(r'^admin/submit$', views.submit, name='submit'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        url(r'^404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        )
