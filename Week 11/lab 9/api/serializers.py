from rest_framework import serializers
from api.models import Company, Vacancy
from django.contrib.auth.models import User


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'),
                                         description=validated_data.get('description'),
                                         city=validated_data.get('city'),
                                         address=validated_data.get('address'))
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    salary = serializers.CharField()
    company = CompanySerializer()

    def create(self, validated_data):
        vacancy = Vacancy.objects.create(name=validated_data.get('name'),
                                         description=validated_data.get('description'),
                                         salary=validated_data.get('salary'),
                                         company=validated_data.get('company'))
        return vacancy

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.desciption)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.company = validated_data.get('company', instance.city)
        instance.save()
        return instance


class VacancySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class CompanyWithVacanciesSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # products = serializers.StringRelatedField(many=True, read_only=True)
    products = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'products',)
