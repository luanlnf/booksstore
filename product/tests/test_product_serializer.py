import pytest
from product.models.product import Product
from product.models.category import Category
from product.serializers.product_serializer import ProductSerializer


@pytest.mark.django_db
def test_product_serializer_representation():
    cat1 = Category.objects.create(title="Eletrônicos", slug="eletronicos", description="desc", active=True)
    cat2 = Category.objects.create(title="Games", slug="games", description="desc", active=True)

    product = Product.objects.create(
        title="PlayStation 5",
        description="Console da Sony",
        price=4999.90,
        active=True
    )
    product.categorie.add(cat1, cat2)

    serializer = ProductSerializer(product)
    data = serializer.data

    assert set(data.keys()) == {"id", "title", "description", "price", "active", "categorie"}
    assert data["title"] == "PlayStation 5"
    assert len(data["categorie"]) == 2
    assert data["categorie"][0]["title"] in ["Eletrônicos", "Games"]


@pytest.mark.django_db
def test_product_serializer_create_valid():
    cat = Category.objects.create(title="Informática", slug="informatica", description="desc", active=True)
    data = {
        "title": "Notebook Dell",
        "description": "Laptop com 16GB RAM",
        "price": 3500.00,
        "active": True,
        "categorie": [cat.id]
    }

    serializer = ProductSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    product = serializer.save()
    assert product.title == "Notebook Dell"
    assert product.categorie.count() == 1
