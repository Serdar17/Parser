import asyncio
import datetime

from .price_nout_request import start_parser
import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}


async def periodic():
    while True:
        print("Background worker started at ", datetime.datetime.now())
        products = start_parser()

        def send_data_task():
            for product in products:
                json_data = {
                    'name': product["name"],
                    'description': product["description"],
                    'price': product["price"],
                }

                response = requests.post('http://127.0.0.1:8000/product/', headers=headers, json=json_data)

        loop = asyncio.get_running_loop()
        awaitable = loop.run_in_executor(None, send_data_task)
        await asyncio.sleep(86400)
