from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Profile

User = get_user_model()

class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Your password must be at least 8-characters long')

        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Your password inputs don\'t match')

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')

        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'age', 'email', 'contact_number']
