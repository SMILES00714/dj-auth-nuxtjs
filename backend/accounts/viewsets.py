# backend.accounts.viewsets.py

from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from accounts import serializers

USER = get_user_model()


class CustomUserModelViewSet(viewsets.ModelViewSet):
    queryset = USER.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CustomUserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
