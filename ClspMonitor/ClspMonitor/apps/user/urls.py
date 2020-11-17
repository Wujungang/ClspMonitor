from django.conf.urls import url
from django.views.generic import RedirectView
from user import views


urlpatterns = [

    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameCountView.as_view()),
    url(r'^users/$', views.UserView.as_view()),
]
