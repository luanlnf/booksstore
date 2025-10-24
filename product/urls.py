from django.urls import path, include
from rest_framework import routers

from product.viewsets import product_viewset, category_viewset

router = routers.SimpleRouter()
router.register(r'product', product_viewset.ProductViewSet, basename='product')
router.register(r'category', category_viewset.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
