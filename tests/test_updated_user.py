from endpoints.updated_user import UpdatedUser


class TestUpdatedUser:

    def test_updated_user(self, create_user):
        self.user_updater = UpdatedUser()
        self.user_updater.updated_user(create_user)