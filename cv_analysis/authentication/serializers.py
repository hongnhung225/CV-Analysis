from rest_framework import serializers
from authentication.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        validated_data['username'] = validated_data['email']       
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'token']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        read_only_fields = ['token']