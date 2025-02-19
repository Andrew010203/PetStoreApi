import requests
import allure
import pytest
from faker import Faker

fake = Faker()

HOST = 'https://petstore.swagger.io/v2'


class GetUserByUserName:

    @allure.step('Get user by user name')
    def get_user_by_user_name(self, username):
        """Получить пользователя по имени пользователя"""
        payload = {}
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(f"{HOST}/user/{username}", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        print(response.json())
        assert 'id' in response.json(), "there is no 'id' in response"
        assert 'username' in response.json(), "there is no 'username' in response"
        assert 'firstName' in response.json(), "there is no 'firstName' in response"
        assert 'lastName' in response.json(), "there is no 'lastName' in response"
        assert 'email' in response.json(), "there is no 'email' in response"
        assert 'password' in response.json(), "there is no 'password' in response"
        assert 'phone' in response.json(), "there is no 'phone' in response"
        assert 'userStatus' in response.json(), "there is no 'userStatus' in response"