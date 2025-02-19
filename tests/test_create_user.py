from endpoints.create_user import CreateUser


class TestCreateUser:

    def test_create_user(self):
        self.user_creator = CreateUser()
        self.user_creator.create_user()