import json

import factory
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


from django.urls import reverse

from product.factories import ProductFactory, CategoryFactory
from order.factories import UserFactory
from product.models import Product


class TestProductViewset(APITestCase):

    client = APIClient()

    def setUp(self):
        self.user = UserFactory()

        self.product = ProductFactory(title="pro controller", price=200.0)

    def test_get_all_products(self):

        respose = self.client.get(reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(respose.status_code, status.HTTP_200_OK)
        product_data = json.loads(respose.content)

        self.assertEqual(product_data["results"][0]["title"], self.product.title)
        self.assertEqual(product_data["results"][0]["price"], self.product.price)
        self.assertEqual(product_data["results"][0]["active"], self.product.active)

    def test_create_product(self):

        category = CategoryFactory()

        data = json.dumps(
            {"title": "nootebook", "price": 800.0, "categories_id": [category.id]}
        )
        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title="nootebook")

        self.assertEqual(created_product.title, "nootebook")
        self.assertEqual(created_product.price, 800.0)
