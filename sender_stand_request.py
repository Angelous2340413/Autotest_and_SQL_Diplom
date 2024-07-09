#Ангелина Купцова, 18-когорта - Финальный проект. Инженер по тестированию плюс
import configuration
import data
import requests

# Функция для создания заказа
def create_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH, json= data.order_data)
    return response

# Функция для получения заказа по треку
def get_order_by_track(track_number):
    # Добавляем трек как параметр запроса
    response = requests.get(f"{configuration.URL_SERVICE}{configuration.ORDER_NUMBER}?t={track_number}")
    return response

#Ангелина Купцова, 18-когорта - Финальный проект. Инженер по тестированию плюс
# Тест для создания заказа и проверки получения заказа по треку
def test_create_and_get_order():
    # Шаг 1: Создание заказа
    create_response = create_order()
    assert create_response.status_code == 201

    # Сохранение номера трека
    track_number = create_response.json().get("track")
    assert track_number is not None

    # Шаг 2: Получение заказа по треку
    get_response = get_order_by_track(track_number)
    assert get_response.status_code == 200

