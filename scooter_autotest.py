# Киц Алексей, 41-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

BASE_URL = "https://899cfad3-67bf-47a8-aa20-43b181785590.serverhub.praktikum-services.ru"

order_data = {
    "firstName": "Alex",
    "lastName": "Kits",
    "address": "ulitsa",
    "metroStation": 4,
    "phone": "89999999997",
    "rentTime": 5,
    "deliveryDate": "2026-06-06",
}

create_response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_data, headers={"Content-Type": "application/json"})

if create_response.status_code == 201:
    track = create_response.json()["track"]
    get_response = requests.get(f"{BASE_URL}/api/v1/orders/track", params={"t": track})
    if get_response.status_code == 200:
        print(get_response.status_code)