import pytest
import requests
import random
from faker import Faker

fake = Faker()

HOST = 'https://petstore.swagger.io/v2'


@pytest.fixture(scope="function")
def add_a_new_pet_to_the_store():
    """Предмет для питомца, который необходимо добавить в магазин"""
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
    print(response.json())
    pet_id = response.json()['id']
    yield pet_id