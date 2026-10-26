"""Model test examples for Product CRUD and query methods.

Merge these methods into the original project's Product model test class.
The original project's setUp/tearDown and database reset fixture may be required.
"""

from tests.factories import ProductFactory
from service.models import Product


def test_read_update_delete_list_and_filters_require_original_test_fixture():
    """Placeholder reminder: use the project's original unittest test class."""
    # This file intentionally does not pretend to be a standalone runnable test.
    # Copy the methods below into the existing Product model test class.
    pass


# Methods to merge into the original Product model test class:
#
# def test_read_a_product(self):
#     product = ProductFactory()
#     product.id = None
#     product.create()
#     found = Product.find(product.id)
#     self.assertIsNotNone(found)
#     self.assertEqual(found.id, product.id)
#     self.assertEqual(found.name, product.name)
#     self.assertEqual(found.description, product.description)
#     self.assertEqual(found.price, product.price)
#     self.assertEqual(found.available, product.available)
#     self.assertEqual(found.category, product.category)
#
# def test_update_a_product(self):
#     product = ProductFactory()
#     product.id = None
#     product.create()
#     original_id = product.id
#     product.description = "testing"
#     product.update()
#     self.assertEqual(product.id, original_id)
#     found = Product.find(original_id)
#     self.assertIsNotNone(found)
#     self.assertEqual(found.description, "testing")
#     self.assertEqual(len(Product.all()), 1)
#
# def test_delete_a_product(self):
#     product = ProductFactory()
#     product.create()
#     product_id = product.id
#     product.delete()
#     self.assertIsNone(Product.find(product_id))
#
# def test_list_all_products(self):
#     products = ProductFactory.create_batch(5)
#     found = Product.all()
#     self.assertEqual(len(found), 5)
#
# def test_find_by_name(self):
#     for _ in range(5):
#         product = ProductFactory()
#         product.id = None
#         product.name = "Laptop"
#         product.create()
#     found = Product.find_by_name("Laptop")
#     self.assertEqual(len(found), 5)
#     self.assertTrue(all(p.name == "Laptop" for p in found))
#
# def test_find_by_category(self):
#     for _ in range(10):
#         product = ProductFactory()
#         product.id = None
#         product.category = "Electronics"
#         product.create()
#     found = Product.find_by_category("Electronics")
#     self.assertEqual(len(found), 10)
#
# def test_find_by_availability(self):
#     for i in range(10):
#         product = ProductFactory()
#         product.id = None
#         product.available = i < 6
#         product.create()
#     found = Product.find_by_availability(True)
#     self.assertEqual(len(found), 6)
