from django.conf.urls import url
from AirlineTicketApp.views import index, login_view, logout_view, \
    register_user_view,ticket_book_view, book_info_view

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_user_view, name='register'),
    url(r'^ticket_book/$', ticket_book_view, name='ticket_book'),
    url(r'^book_info/$', book_info_view, name=' book_info')
]



