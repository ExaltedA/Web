from rest_framework import serializers
from core.models import *
from django.contrib.auth.models import User


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    image = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        product = Product.objects.create(name=validated_data.get('name'),
                                         description=validated_data.get('description'),
                                         image=validated_data.get('image'),
                                         price=validated_data.get('price'))
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ProductSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer = serializers.CharField()
    date_created = serializers.CharField()
    status = serializers.FloatField()
    note = serializers.CharField()

    def create(self, validated_data):
        order = Order.objects.create(name=validated_data.get('name'),
                                     customer=validated_data.get('customer'),
                                     date_created=validated_data.get('date_created'),
                                     status=validated_data.get('status'),
                                     note=validated_data.get(''))
        return order

    def update(self, instance, validated_data):
        instance.customer = validated_data.get('name', instance.name)
        instance.date_created = validated_data.get('description', instance.description)
        instance.status = validated_data.get('image', instance.image)
        instance.note = validated_data.get('price', instance.price)
        instance.save()
        return instance


class OrderSerializer2(serializers.ModelSerializer):
    #
    class Meta:
        model = Order
        fields = '__all__'
