from django.contrib import admin
from django.urls import path





urlpatterns = [
    path('admin/', admin.site.urls),
    path('perpus/', perpus),
    path('nama/', nama),
]
