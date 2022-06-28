# backend.core.urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('customer/account/', include('accounts.urls')),

    path('', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
]
