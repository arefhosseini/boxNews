from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'boxNewsApp.views.home', name='home'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^varzesh/(?P<pageNumber>[1-9][0-9]{0,10})$', 'boxNewsApp.views.varzesh'),
    url(r'^movie/(?P<pageNumber>[1-9][0-9]{0,10})$', 'boxNewsApp.views.movie'),
    url(r'^music/(?P<pageNumber>[1-9][0-9]{0,10})$', 'boxNewsApp.views.music'),
    url(r'^game/(?P<pageNumber>[1-9][0-9]{0,10})$', 'boxNewsApp.views.game'),
    url(r'^signup/$', 'boxNewsApp.views.signup'),
    url(r'^forgotPass/$', 'boxNewsApp.views.forgotPass'),
    url(r'^success/$', 'boxNewsApp.views.success'),
    url(r'^login/$', 'boxNewsApp.views.login_user'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^exituser/', 'boxNewsApp.views.exituser'),
    url(r'^profile/', 'boxNewsApp.views.profile'),
    url(r'^sendComment/', 'boxNewsApp.views.sendComment'),
    url(r'^confirm/(?P<confirmation_code>[\w]{32})/(?P<username>[\w]{0,200})$', 'boxNewsApp.views.confirm',
        name='user_confirm')
]
