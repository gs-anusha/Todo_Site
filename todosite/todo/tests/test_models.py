from utils.setup_test import TestSetUp
from todo.models import Todo


class TestModel(TestSetUp):

    def test_should_create_user(self):
        user = self.create_test_user()
        todo = Todo(title="title",
                    description="description",
                    is_completed=False,
                    owner=user)
        todo.save()
        self.assertEqual(str(todo), 'title')
