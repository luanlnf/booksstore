import factory
from django.contrib.auth.models import User
from order.models import Order
from product.factories import ProductFactory


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    username = factory.Faker("user_name")

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)

    @factory.post_generation
    def save_after(self, create, extracted, **kwargs):
        """Salva manualmente após postgeneration (evita o warning do factory_boy)."""
        if create:
            self.save()

    class Meta:
        model = Order
        skip_postgeneration_save = True
