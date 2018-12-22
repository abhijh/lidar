from django.conf.urls import url, include
from download import views

urlpatterns = [
    url(r'^$', views.download),
    url(r'^progress/(?P<pid>\d+)/$', views.get_progress_for_task),
]
