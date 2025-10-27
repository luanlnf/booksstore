import factory
from product.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    title = factory.Faker("pystr")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)

    @factory.post_generation
    def save_after(self, create, extracted, **kwargs):
        """Salva manualmente após postgeneration (evita o warning do factory_boy)."""
        if create:
            self.save()

    class Meta:
        model = Product
        skip_postgeneration_save = True
