from django.conf.urls import url
from django.views.generic import RedirectView
from verifications import views
from clsp.views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^$', index),
    url('^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCodeView.as_view()),
    url('^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view()),

    url(r'^middleware$', middleware),

]

router = DefaultRouter()
router.register(r'^nodes',NodeInfoViewSet)
urlpatterns += router.urls