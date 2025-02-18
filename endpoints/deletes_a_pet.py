import requests
import allure

HOST = 'https://petstore.swagger.io/v2'


class DeletesAPet:

    @allure.step('Deletes a pet')
    def deletes_a_pet(self, pet_id):
        """Удалить питомца по id"""
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'api_key': 'special-key'
        }
        response = requests.delete(f"{HOST}/pet/{pet_id}", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        # Проверка, удалился ли ранее удаленный питомец
        response = requests.get(f"{HOST}/pet/{pet_id}", headers=headers, json=payload)
        assert response.status_code == 404, response.status_code