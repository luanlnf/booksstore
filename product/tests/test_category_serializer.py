import pytest
from product.serializers.category_serializer import CategorySerializer
from product.models.category import Category


@pytest.mark.django_db
def test_category_serializer_fields():
    category = Category.objects.create(
        title="Eletrônicos",
        slug="eletronicos",
        description="Produtos eletrônicos em geral",
        active=True
    )

    serializer = CategorySerializer(category)
    data = serializer.data

    assert set(data.keys()) == {"title", "slug", "description", "active"}
    assert data["title"] == "Eletrônicos"
    assert data["slug"] == "eletronicos"
    assert data["description"] == "Produtos eletrônicos em geral"
    assert data["active"] is True


@pytest.mark.django_db
def test_category_serializer_validation():
    data = {
        "title": "",
        "slug": "sem-titulo",
        "description": "Categoria sem título",
        "active": True
    }
    serializer = CategorySerializer(data=data)
    assert not serializer.is_valid()
    assert "title" in serializer.errors
