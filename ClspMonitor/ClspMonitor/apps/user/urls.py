from django.conf.urls import url
from django.views.generic import RedirectView
from user import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameCountView.as_view()),

]
