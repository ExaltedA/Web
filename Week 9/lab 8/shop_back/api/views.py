from django.http.response import JsonResponse
from api.models import Product, Category
from django.http import Http404


def hello(request):
    return JsonResponse('HELLO MAAN, GO TO API OR ADMIN!', safe=False)


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.to_json())


def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())


def category_products(request, cat_id):
    try:
        products = Product.objects.all()
        related = []
        for product in products:
            if product.category_id.id == cat_id:
                related.append(product.to_json())
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if related:
        return JsonResponse(related, safe=False)
    else:
        return JsonResponse('Category doesn\'t exists', safe=False)

# def category_products(request, cat_id):
#     try:
#         related = Product.objects.get(category_id_id=cat_id)
#     except Product.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#
#     return JsonResponse(related.to_json(), safe=False)
