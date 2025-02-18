import requests
import allure

HOST = 'https://petstore.swagger.io/v2'


class FindPurchaseOrderById:

    @allure.step('Find purchase order by id')
    def find_purchase_order_by_id(self, order_id):
        """Найти заказ на покупку по id"""
        payload = {}
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(f"{HOST}/store/order/{order_id}", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        print(response.json())
        assert 10 >= order_id >= 1, "wrong order_id!"