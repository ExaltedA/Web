from rest_framework import serializers
from core.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class CommentSerializer(serializers.Serializer):
    user = UserSerializer()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

class ProductSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
