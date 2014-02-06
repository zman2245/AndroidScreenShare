from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'setscreen', 'android_screen_share.views.setscreen'),
    url(r'getscreen', 'android_screen_share.views.getscreen'),
    url(r'getimage', 'android_screen_share.views.getimage', name='getimage'),
    url(r'click/', include('screen.urls', namespace='screen')),
    url(r'screen/', include('screen.urls', namespace='screen')),
    # Examples:
    # url(r'^$', 'android_screen_share.views.home', name='home'),
    # url(r'^android_screen_share/', include('android_screen_share.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
