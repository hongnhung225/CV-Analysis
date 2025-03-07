from rest_framework import serializers
from authentication.models import User

class RegisterSerializer(serializers.ModelSerializer):

    # password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'token']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        read_only_fields = ['token']