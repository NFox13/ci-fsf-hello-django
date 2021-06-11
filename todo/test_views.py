from django.test import TestCase
from .models import item


class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
    
    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        itema = item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{itema.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')
    
    def test_can_add_item(self):
        response = self.client.post('/add',{'name':'Test Added Item'})
        self.assertRedirects(response, '/')
    
    def test_can_delete_item(self):
        itema = item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{itema.id}')
        self.assertRedirects(response, '/')
        existing_items = item.objects.filter(id=itema.id)
        self.assertEqual(len(existing_items),0)
    
    def test_can_toggle_item(self):
        itema = item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{itema.id}')
        self.assertRedirects(response, '/')
        updated_itema = item.objects.get(id=itema.id)
        self.assertFalse(updated_itema.done)

    def test_can_edit_item(self):
        itema = item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{itema.id}', {'name':'Updated Name'})
        self.assertRedirects(response, '/')
        updated_itema = item.objects.get(id=itema.id)
        self.assertEqual(updated_itema.name, 'Updated Name')
