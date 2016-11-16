#!/usr/bin/env python
import requests


def http_json_post(url, json):
    custom_header = {"Content-Type": "application/json"}
    return requests.post(url,
                         json=json,
                         timeout=0.1,
                         headers=custom_header)


def get_order_grand_total(order_json):
    try:
        url = 'http://127.0.0.1:8000/api/order-total'
        response = http_json_post(url, order_json)
        if response.status_code == 200:
            order_total = response.json()
            print(order_total['grand_total'])
        else:
            print('Not OK')
    except requests.ConnectionError:
        print('Not OK, Connect Error')
    except requests.ConnectTimeout:
        print('Not OK, Connection Timeout')


if __name__ == '__main__':
    order_data = {
        "order_id": 123,
        "items_total": 100.0,
        "options": [
            {"name": "bacon", "price": 1.0},
            {"name": "ham", "price": 2.0}
        ]
    }
    get_order_grand_total(order_data)
