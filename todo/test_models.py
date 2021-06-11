from django.test import TestCase
from .models import item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        itema = item.objects.create(name='Test Todo Item')
        self.assertFalse(itema.done)

    def test_item_string_method_returns_name(self):
        itema = item.objects.create(name='Test Todo Item')
        self.assertEqual(str(itema),'Test Todo Item')
