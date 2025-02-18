import requests
import allure

HOST = 'https://petstore.swagger.io/v2'


class ReturnsPetInventoryByStatus:

    @allure.step('Returns pet inventory by status')
    def returns_pet_inventory_by_status(self):
        """Возвращает инвентарь питомцев по статусу"""
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'api_key': 'special-key'
        }
        response = requests.get(f"{HOST}/store/inventory", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        print(response.json())
        assert response.json() != 0 or response.json() != '', "Response is empty"