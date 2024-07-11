#Ангелина Купцова, 18-когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def test_create_and_get_order():
    # Шаг 1: Создание заказа
    create_response = sender_stand_request.create_order()
    assert create_response.status_code == 201

    # Сохранение номера трека
    track_number = create_response.json().get("track")
    assert track_number is not None

    # Шаг 2: Получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track_number)
    assert get_response.status_code == 200