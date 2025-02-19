import requests
import allure

HOST = 'https://petstore.swagger.io/v2'


class DeletePurchaseOrderById:

    @allure.step('Delete purchase order by id')
    def delete_purchase_order_by_id(self, order_id):
        """Удалить заказ на покупку по id"""
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'api_key': 'special-key'
        }
        response = requests.delete(f"{HOST}/store/order/{order_id}", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        # Проверка, удалился ли ранее удаленный заказ на покупку по id
        response = requests.get(f"{HOST}/store/order/{order_id}", headers=headers, json=payload)
        assert response.status_code == 404, response.status_code