from django_filters import rest_framework as filters

from core.models import Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    price = filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Product
        fields = ('name', 'price')
