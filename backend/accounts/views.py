# backend.accounts.views.py

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from accounts import serializers

USER = get_user_model()


class UserRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = USER.objects.all()
    serialier_class = serializers.CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
