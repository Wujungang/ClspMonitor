from django.conf.urls import url
from clsp.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^middleware$', middleware),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^user_count/$', user_count),
    url(r'^user_list/$', user_list),
    url(r'^news_review/$', user_list)

]