from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class CompaniesList(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompaniesDetail(APIView):
    def get_object(self, comp_id):
        try:
            return Company.objects.get(id=comp_id)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, comp_id):
        company = self.get_object(comp_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, comp_id):
        company = self.get_object(comp_id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, comp_id):
        company = self.get_object(comp_id)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VacanciesList(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer2(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VacancySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VacanciesDetail(APIView):
    def get_object(self, vacant_id):
        try:
            return Vacancy.objects.get(id=vacant_id)
        except Vacancy.DoesNotExist:
            raise Http404

    def get(self, request, vacant_id):
        vacancy = self.get_object(vacant_id)
        serializer = VacancySerializer2(vacancy)
        return Response(serializer.data)

    def put(self, request, vacant_id):
        vacancy = self.get_object(vacant_id)
        serializer = VacancySerializer2(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, vacant_id):
        vacancy = self.get_object(vacant_id)
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
