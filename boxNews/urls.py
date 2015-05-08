from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'boxNewsApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^varzesh/$', 'boxNewsApp.views.varzesh'),
    url(r'^movie/$', 'boxNewsApp.views.movie'),
    url(r'^music/$', 'boxNewsApp.views.music'),
    url(r'^game/$', 'boxNewsApp.views.game'),
    url(r'^admin/', include(admin.site.urls)),
]
