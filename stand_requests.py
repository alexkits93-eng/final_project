import requests
import configuration
import data

def post_new_order(body):
    return requests.post(
        configuration.BASE_URL + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers
    )

def get_order_by_track(track):
    return requests.get(
        configuration.BASE_URL + configuration.GET_ORDER_PATH,
        params={"t": track}
    )