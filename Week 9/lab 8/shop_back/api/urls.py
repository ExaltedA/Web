from django.urls import path

from api.views import *

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail),
    path('categories/<int:cat_id>/products', category_products),

]
