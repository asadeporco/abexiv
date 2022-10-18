from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_verified",
        ]

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
        }
        
class UserShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "is_verified",
        ]
