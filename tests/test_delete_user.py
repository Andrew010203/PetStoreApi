from endpoints.delete_user import DeleteUser


class TestDeleteUser:

    def test_delete_user(self, create_user):
        self.user_deleter = DeleteUser()
        self.user_deleter.delete_user(create_user)