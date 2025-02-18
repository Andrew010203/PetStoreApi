import requests
import allure
import pytest
from faker import Faker

fake = Faker()

HOST = 'https://petstore.swagger.io/v2'


class FindPetsByStatus:

    @allure.step('Find pets by status')
    def find_pets_by_status(self, status):
        """Найти питомцев по статусу"""
        payload = {}
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(f"{HOST}/pet/findByStatus?status={status}", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        print(response.json())
        pets = response.json()
        # Проверяем статус каждого питомца
        for pet in pets:
            assert pet['status'] == status, "status does not match"
