from django.urls import include, path
from rest_framework import routers

from .views import MessageViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
