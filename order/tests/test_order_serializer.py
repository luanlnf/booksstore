import pytest
from product.models.product import Product
from product.models.category import Category
from order.serializers.order_serializer import OrderSerializer


@pytest.mark.django_db
def test_order_serializer_total_field():
    cat = Category.objects.create(title="Acessórios", slug="acessorios", description="desc", active=True)

    p1 = Product.objects.create(title="Mouse", description="Óptico", price=100.0, active=True)
    p2 = Product.objects.create(title="Teclado", description="Mecânico", price=200.0, active=True)
    p1.categorie.add(cat)
    p2.categorie.add(cat)

    # Simula um objeto com ManyToMany
    class FakeOrder:
        def __init__(self, products):
            self.product = products

    order = FakeOrder(Product.objects.filter(id__in=[p1.id, p2.id]))

    serializer = OrderSerializer(order)
    data = serializer.data

    assert "total" in data
    assert data["total"] == 300.0  # 100 + 200
    assert len(data["product"]) == 2
