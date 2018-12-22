from django.conf.urls import url, include
from rest_framework import routers
from music import views

router = routers.SimpleRouter()
router.register(r'album', views.AlbumViewSet)
router.register(r'track', views.TrackViewSet)

urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^search-album-details/$', views.fetch_album_details),
] + router.urls
