import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company
from api.models import Vacancy


@csrf_exempt
def companies_list1(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        cmp_json = [company.to_json() for company in companies]
        return JsonResponse(cmp_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        company = Company.objects.create(name=data.get('name', 'default_name'),
                                         description=data.get('description', 'default_desc'),
                                         city=data.get('city', 'default_city'),
                                         address=data.get('address', 'default_address'))
        return JsonResponse(company.to_json())


def companies_detail(request, comp_id):
    try:
        company = Company.objects.get(id=comp_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(company.to_json())


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(vacancy.to_json())


def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExitst as e:
        return JsonResponse({'error': str(e)})
    vacancies = company.vacancy_set.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:5]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
