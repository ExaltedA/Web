from django.urls import path
from api.views import *

urlpatterns = [
    path('', hello),
    path('companies/', companies_list),
    path('companies/<int:comp_id>/', companies_detail),
    path('companies/<int:comp_id>/vacancies', companies_vacancies),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacant_id>/', vacancies_detail),
    path('vacancies/top_ten/', vacancies_top)
]
