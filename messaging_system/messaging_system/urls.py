from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('foradmin/', admin.site.urls),
]
