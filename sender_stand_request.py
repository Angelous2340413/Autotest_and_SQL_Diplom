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


