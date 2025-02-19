import requests
import allure
import random
from faker import Faker

fake = Faker()

HOST = 'https://petstore.swagger.io/v2'


class CreateListOfUsersWithGivenInputArray:

    @allure.step('Create list of users with given input array')
    def create_list_of_users_with_given_input_array(self):
        """Создает список пользователей с заданным входным массивом"""
        payload = [{
                    "id": random.randint(1, 99),
                    "username": fake.user_name(),
                    "firstName": fake.first_name(),
                    "lastName": fake.last_name(),
                    "email": fake.email(),
                    "password": fake.password(length=10),
                    "phone": fake.phone_number(),
                    "userStatus": random.randint(1, 99)
                }]
        headers = {
            'Content-Type': 'application/json',
            'api_key': 'special-key'
        }
        response = requests.post(f"{HOST}/user/createWithList", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        print(response.json())
        assert 'code' in response.json(), "there is no 'code' in response"
        assert 'type' in response.json(), "there is no 'type' in response"
        assert 'message' in response.json(), "there is no 'message' in response"