from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'login', 
            'password', 
            'avatar', 
            'thumbnail', 
            'youtubeLink', 
            'vkLink', 
            'tgLink',
            ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            login=validated_data['login'],
            password=validated_data['password']
        )
        return user
