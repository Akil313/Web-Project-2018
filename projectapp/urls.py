from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]