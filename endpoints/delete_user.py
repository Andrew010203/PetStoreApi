import requests
import allure

HOST = 'https://petstore.swagger.io/v2'


class DeleteUser:

    @allure.step('Delete user')
    def delete_user(self, username):
        """Удалить пользователя"""
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'api_key': 'special-key'
        }
        response = requests.delete(f"{HOST}/user/{username}", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        # Проверка, удалился ли ранее удаленный пользователь
        response = requests.get(f"{HOST}/pet/{username}", headers=headers, json=payload)
        assert response.status_code == 404, response.status_code
        print(response.status_code)