import requests
import allure
import random
from faker import Faker

fake = Faker()

HOST = 'https://petstore.swagger.io/v2'


class AddANewPetToTheStore:

    @allure.step('Add a new pet to the store')
    def add_a_new_pet_to_the_store(self):
        """Добавить нового питомца в магазин"""
        payload = {
            "id": random.randint(1, 99),
            "category": {
                "id": random.randint(1, 99),
                "name": fake.name()
            },
            "name": fake.user_name(),
            "photoUrls": [
                fake.image_url()
            ],
            "tags": [
                {
                    "id": random.randint(1, 99),
                    "name": fake.name()
                }
            ],
            "status": "available"
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(f"{HOST}/pet", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        print(response.json())
        assert response.json()['id'] == payload['id'], "wrong id!"
        assert response.json()['category']['id'] == payload['category']['id'], "wrong id!"
        assert response.json()['category']['name'] == payload['category']['name'], "wrong name!"
        assert response.json()['name'] == payload['name'], "wrong name!"
        assert response.json()['photoUrls'] == payload['photoUrls'], "wrong photoUrls!"
        assert response.json()['tags'][0]['id'] == payload['tags'][0]['id'], "wrong id!"
        assert response.json()['tags'][0]['name'] == payload['tags'][0]['name'], "wrong name!"
        assert response.json()['status'] == payload['status'], "wrong status!"
