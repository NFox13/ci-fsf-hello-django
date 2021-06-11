from django.test import TestCase
from .models import item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        itema = item.objects.create(name='Test Todo Item')
        self.assertFalse(itema.done)