from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('foradmin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api'))
]
