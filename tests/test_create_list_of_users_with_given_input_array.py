from endpoints.create_list_of_users_with_given_input_array import CreateListOfUsersWithGivenInputArray


class TestCreateListOfUsersWithGivenInputArray:

    def test_create_list_of_users_with_given_input_array(self):
        self.user_list_creator = CreateListOfUsersWithGivenInputArray()
        self.user_list_creator.create_list_of_users_with_given_input_array()