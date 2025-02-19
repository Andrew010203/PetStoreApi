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


@pytest.fixture(scope="function")
def place_an_order_for_a_pet():
    """Оформить заказ на питомца"""
    payload = {
        "id": random.randint(1, 10),
        "petId": random.randint(1, 99),
        "quantity": random.randint(1, 99),
        "shipDate": fake.date(),
        "status": "placed",
        "complete": True
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(f"{HOST}/store/order", headers=headers, json=payload)
    assert response.status_code == 200, response.status_code
    print(response.json())
    order_id = response.json()['id']
    yield order_id


@pytest.fixture(scope="function")
def create_user():
    """Создать пользователя"""
    payload = {
                "id": random.randint(1, 99),
                "username": fake.user_name(),
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "email": fake.email(),
                "password": fake.password(),
                "phone": fake.phone_number(),
                "userStatus": random.randint(1, 99)
            }
    headers = {
        'Content-Type': 'application/json',
        'api_key': 'special-key'
    }
    response = requests.post(f"{HOST}/user", headers=headers, json=payload)
    assert response.status_code == 200, response.status_code
    print(response.json())
    assert 'code' in response.json(), "there is no 'code' in response"
    assert 'type' in response.json(), "there is no 'type' in response"
    assert 'message' in response.json(), "there is no 'message' in response"
    username = payload['username']
    yield username