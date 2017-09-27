from django.conf.urls import url
from AirlineTicketApp.views import index, login_view, logout_view


urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout')
]