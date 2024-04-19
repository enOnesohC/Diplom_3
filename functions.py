import random
import string
import requests
from test_page_object.urls import URLS


class Functions:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def create_new_user():
        superbody = []

        email = Functions.generate_random_string(8) + "@yandex.ru"
        password = Functions.generate_random_string(8)
        name = Functions.generate_random_string(8)

        body = \
            {
                "email": email,
                "password": password,
                "name": name
            }

        responce = requests.post(URLS.URL_CREATE_USER, json=body)
        atoken = responce.json()["accessToken"]
        if responce.status_code == 200:
            superbody.append(email)
            superbody.append(password)
            superbody.append(name)
            superbody.append(atoken)

        return superbody

    @staticmethod
    def create_order_with_auth_with_ingr(create_user):
        """
        создаём тело запроса, затем авторизуемся, создаём заказ
        и возвращаем запрос
        :param create_user:
        :return:
        """
        header = \
            {
                'Authorization': create_user[3]
            }

        body = \
            {
                "email": create_user[0],
                "password": create_user[1],
                "name": create_user[2]
            }
        requests.post(URLS.URL_AUTHORIZATION, json=body, headers=header)

        responce_ingredients = requests.get(URLS.URL_CREATE_ORDER)
        ingredients = responce_ingredients.json()["data"]

        body_order = \
            {
                "ingredients": [ingredients[0]["_id"], ingredients[1]["_id"]]
            }

        responce = requests.post(URLS.URL_GET_ORDERS_USER, json=body_order, headers=header)
        return responce
