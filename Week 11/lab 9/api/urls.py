from django.urls import path
# from api.views import *
from rest_framework_jwt.views import obtain_jwt_token
from api.views_generic import *
from api.views_fbv import *
from api.views_cbv import *

# urlpatterns = [
#     # path('', hello),
#     path('login/', obtain_jwt_token),
#     path('companies/', companies_list),
#     path('companies/<int:comp_id>/', companies_detail),
#     path('companies/<int:comp_id>/vacancies', companies_vacancies),
#     path('vacancies/', vacancies_list),
#     path('vacancies/<int:vacant_id>/', vacancies_detail),
#     # path('vacancies/top_ten/', vacancies_top)
# ]
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('vacancies/', VacanciesList.as_view()),
    path('vacancies/<int:vacant_id>/', VacanciesDetail.as_view()),
    path('companies/', CompaniesList.as_view()),
    path('companies/<int:comp_id>/', CompaniesDetail.as_view()),
    # path('vacancies/top_ten/', top_ten_vacancies)
]

# urlpatterns = [
#     path('login/', obtain_jwt_token),
#     path('vacancies/', VacancyListAPIView.as_view()),
#     path('vacancies/<int:vacant_id>/', VacancyDetailAPIView.as_view()),
#     path('companies/', CompanyListAPIView.as_view()),
#     path('companies/<int:comp_id>/', CompanyDetailAPIView.as_view()),
#     # path('companies/<int:comp_id>/vacancies/', company_vacancies),
#     # path('vacancies/top_ten/', top_ten_vacancies)
# ]