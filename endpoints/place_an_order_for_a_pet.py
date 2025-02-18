import requests
import allure
import random
from faker import Faker

fake = Faker()

HOST = 'https://petstore.swagger.io/v2'


class PlaceAnOrderForAPet:

    @allure.step('Place an order for a pet')
    def place_an_order_for_a_pet(self):
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
        assert response.json()['id'] == payload['id'], "wrong id!"
        assert response.json()['petId'] == payload['petId'], "wrong petId!"
        assert response.json()['quantity'] == payload['quantity'], "wrong quantity!"
        date1 = payload['shipDate']
        date2 = response.json()['shipDate']
        print(date1)
        print(date2)
        assert date1[:10] == date2[:10], "wrong shipDate!"
        assert response.json()['status'] == payload['status'], "wrong status!"
        assert response.json()['complete'] == payload['complete'], "wrong complete!"
