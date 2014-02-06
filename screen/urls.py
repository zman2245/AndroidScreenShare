from django.conf.urls import patterns, url
from screen import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'socket', views.SocketView.as_view(), name='socket'),
    url(r'set', 'screen.views.setclick', name='setclick'),
    url(r'all', views.AllView.as_view(), name='all'),
    url(r'new', 'screen.views.newscreen', name='newscreen'),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
