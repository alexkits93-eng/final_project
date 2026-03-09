# Киц Алексей, 41-я когорта — Финальный проект. Инженер по тестированию плюс
import stand_requests
import data

def test_create_and_get_order():
    create_response = stand_requests.post_new_order(data.order_data)
    assert create_response.status_code == 201
    
    track = create_response.json()["track"]
    get_response = stand_requests.get_order_by_track(track)
    
    assert get_response.status_code == 200