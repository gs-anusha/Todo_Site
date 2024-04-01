from utils.setup_test import TestSetUp


class TestModel(TestSetUp):

    def test_should_create_user(self):
        user = self.create_test_user()
        self.assertEqual(str(user), user.email)
