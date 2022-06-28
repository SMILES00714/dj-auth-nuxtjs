# backend.accounts.urls.py

from django.urls import path, include

from accounts import routers, views

urlpatterns = [
    path(
        route='data/',
        view=views.user_retrieve_update_destroy,
        name='user-data'
    ),
    path('users/', include(routers.router.urls)),
]
