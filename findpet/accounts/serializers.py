from xml.dom import ValidationErr
from rest_framework import serializers
from .models import User


class SignUpSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password',
                  'city', 'state', 'country', ]

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists

        if not email_exists:
            raise ValidationErr("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'city', 'state', 'country', ]


class CurrentUserPostsSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'posts']
