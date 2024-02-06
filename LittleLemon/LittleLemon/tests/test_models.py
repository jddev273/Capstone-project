from django.test import TestCase
from restaurant.models import Menu

#TestCase class
class MenuTest(TestCase):
    def test_add_to_menu(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")