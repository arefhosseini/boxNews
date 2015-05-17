from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'boxNewsApp.views.home', name='home'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^varzesh/$', 'boxNewsApp.views.varzesh'),
    url(r'^movie/$', 'boxNewsApp.views.movie'),
    url(r'^music/$', 'boxNewsApp.views.music'),
    url(r'^game/$', 'boxNewsApp.views.game'),
    url(r'^signup/$', 'boxNewsApp.views.signup'),
    url(r'^success/$', 'boxNewsApp.views.success'),
    url(r'^login/$', 'boxNewsApp.views.login_user'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^exituser/', 'boxNewsApp.views.exituser'),
    url(r'^sendComment/', 'boxNewsApp.views.sendComment')
]
