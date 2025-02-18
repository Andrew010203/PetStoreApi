import requests
import allure
from faker import Faker

fake = Faker()

HOST = 'https://petstore.swagger.io/v2'


class FindPetsById:

    @allure.step('Find pet by id')
    def find_pets_by_id(self, pet_id):
        """Найти питомца по id"""
        payload = {}
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(f"{HOST}/pet/{pet_id}", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        print(response.json())
        pet_id_response = response.json()['id']
        print(pet_id_response)
        # Проверка что возвращаемый pet_id от сервера совпадает с запрашиваемом pet_id
        assert pet_id_response == pet_id, "pet_id does not match"