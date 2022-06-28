# backend.accounts.serialiers.py

from django.contrib.auth import get_user_model

from rest_framework import serialiers, validators

USER = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.CharField(
        write_only=True, validators=[validators.UniqueValidator(
            message='This email already exists',
            queryset=CustomUser.objects.all()
        )]
    )
    password = serializers.CharField(
        max_length=255,
        style={'input_type': 'password'},
        write_only=True
    )
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    birth_date = serializers.CharField(required=False)

    class Meta:
        model = USER
        fields = [
            'gender', 'first_name', 'last_name',
            'email', 'bio', 'birth_date', 'password'
        ]


class CustomUserRetrieveSerializer(serializers.ModelSerializer):

    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    class Meta:
        model = USER
        fields = [
            'gender', 'first_name', 'last_name',
            'email', 'bio', 'birth_date', 'id'
        ]
