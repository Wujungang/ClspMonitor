from django.conf.urls import url
from clsp.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^middleware$', middleware),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^user_count/$', UserCount.as_view()),
    url(r'^news_review/$', news_review.as_view()),
    url(r'^news_edit/$', news_edit),
    url(r'^news_type/$', news_type),
    url(r'^pagation/$', pagation),
    url(r'^user_list/$', user_list.as_view()),
    url(r'^tenant_list/$', tenant_list.as_view()),
    url(r'^news_review/news_review_detail/$', news_review_detail),
]