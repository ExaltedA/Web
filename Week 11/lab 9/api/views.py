from django.http.response import JsonResponse
from django.http import Http404
from api.models import *


def hello(request):
    str_ini = 'Welcome Stranger, go to the following addresses:' \
              "/api/companies - List of all Companies" \
              "/api/companies/<int:id>/ - Get one Company" \
              "/api/companies/<int:id>/vacancies/ - List of Vacancies by Company" \
              "/api/vacancies/ - List of all Vacancies" \
              "/api/vacancies/<int:id>/ - Get one Vacancy" \
              "api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary"
    return JsonResponse(str_ini, safe=False)


def companies_list(request):
    companies = Company.objects.all()
    cmp_json = [each.to_json() for each in companies]
    return JsonResponse(cmp_json, safe=False)


def companies_detail(request, comp_id):
    try:
        companies = Company.objects.get(id=comp_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(companies.to_json())


def companies_vacancies(request, comp_id):
    try:
        vacancies = Vacancy.objects.filter(company_id=comp_id)
        vacant_json = [vacancy.to_json() for vacancy in vacancies]
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if vacancies:
        return JsonResponse(vacant_json, safe=False)
    else:
        return JsonResponse('Company doesn\'t exists', safe=False)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacant_json = [vacancy.to_json() for vacancy in vacancies]
    if vacant_json:
        return JsonResponse(vacant_json, safe=False)
    else:
        return JsonResponse("No vacancy available, check for updates later!", safe=False)


def vacancies_detail(request, vacant_id):
    try:
        category = Vacancy.objects.get(id=vacant_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())


def sort_salary(vacant):
    return vacant.salary


def vacancies_top(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacant_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacant_json, safe=False)
    # if vacant_json:
    #     return JsonResponse(vacant_json, safe=False)
    # else:
    #     return JsonResponse("No vacancy available, check for updates later!", safe=False)
