from utils.setup_test import TestSetUp
from django.urls import reverse
from todo.models import Todo


class TestModel(TestSetUp):

    def test_should_create_atodo(self):
        user = self.create_test_user()
        self.client.post(reverse('login'), {
            'username': user.username,
            'password': user.password
        })
        todos = Todo.objects.all()
        self.assertEqual(todos.count(), 0)

        response = self.client.post(reverse('create-todo'), {
            "owner": user,
            "title": "Hello do this",
            "description": "Remember to do this",
            "is_completed": True
        })

        updated_todos = Todo.objects.all()

        self.assertEqual(updated_todos.count(), 1)

        self.assertEqual(response.status_code, 302)
