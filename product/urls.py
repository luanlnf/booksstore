from rest_framework.routers import DefaultRouter
from product.views.category_view import CategoryViewSet
from product.views.product_view import ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
