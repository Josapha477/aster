from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ProfilUser, PostUserMedia, PostUserVente


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfilUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = ProfilUser
        fields = ['id', 'user', 'username', 'bio', 'imgP', 'created_at']
        extra_kwargs = {'user': {'read_only': True}}


class PostUserVenteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = PostUserVente
        fields = ['id', 'user', 'username', 'description', 'prix', 'whatsapp', 'imgV', 'created_at']
        extra_kwargs = {'user': {'read_only': True}}


class PostUserMediaSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = PostUserMedia
        fields = ['id', 'user', 'username', 'description', 'imgM', 'created_at']
        extra_kwargs = {'user': {'read_only': True}}
