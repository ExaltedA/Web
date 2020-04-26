from core.models import *
from core.serializers import CompanySerializer, VacancySerializer2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
