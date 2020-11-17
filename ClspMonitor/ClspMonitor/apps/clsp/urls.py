from django.conf.urls import url
from django.views.generic import RedirectView

from clsp.views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^$', index),

    url(r'^middleware$', middleware),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^user_count/$', UserCount.as_view()),
    url(r'^news_review/$', news_review.as_view()),
    url(r'^news_edit/$', news_edit),
    url(r'^nodes_update/$', NodesUpdate.as_view()),
    url(r'^news_type/$', news_type),
    url(r'^user_list/$', user_list.as_view()),
    url(r'^nodes_list/$', node_list.as_view()),
    url(r'^tenant_list/$', tenant_list.as_view()),
    url(r'^news_review/news_review_detail/$', news_review_detail),
]

router = DefaultRouter()
router.register(r'^nodes',NodeInfoViewSet)
urlpatterns += router.urls