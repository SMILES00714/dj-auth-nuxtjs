# backend.accounts.routers.py

from rest_framework import routers

from accounts import viewsets

router = routers.DefaultRouter()
router.register('', viewsets.customuser_model_viewsets)
