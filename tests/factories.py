"""Factory for creating fake Product objects for tests."""

import factory
from factory import fuzzy

from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake products for testing."""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n + 1)
    name = fuzzy.FuzzyChoice(
        ["Laptop", "Phone", "Tablet", "Keyboard", "Monitor"]
    )
    description = factory.Faker("text", max_nb_chars=100)
    price = fuzzy.FuzzyDecimal(0.5, 2000.0, precision=2)
    available = fuzzy.FuzzyChoice([True, False])
    category = fuzzy.FuzzyChoice(
        [
            Category.ELECTRONICS,
            Category.ACCESSORIES,
            Category.FURNITURE,
            Category.CLOTHING,
            Category.UNKNOWN,
            Category.CLOTHS,
        ]
    )
