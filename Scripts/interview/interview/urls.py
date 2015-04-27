from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

# The order is important

urlpatterns = patterns('',
                       url(r'^$', 'interview.views.home'),
                       url(r'^admin/', include(admin.site.urls))    # Username: alejandro, Password: alejandro
)

# Allow path to static files to be shown
urlpatterns += staticfiles_urlpatterns()