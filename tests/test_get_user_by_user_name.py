from endpoints.get_user_by_user_name import GetUserByUserName


class TestGetUserByUserName:

    def test_get_user_by_user_name(self, create_user):
        self.user_getter = GetUserByUserName()
        self.user_getter.get_user_by_user_name(create_user)