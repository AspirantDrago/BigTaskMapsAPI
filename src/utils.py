from io import BytesIO

import requests

from .secrets import STATIC_MAPS_API


def get_image(longitude: float, latitude: float, scale: float) -> BytesIO:
    URL = 'https://static-maps.yandex.ru/v1'
    params = {
        'apikey': STATIC_MAPS_API,
        'll': f'{longitude},{latitude}',
        'spn': f'{scale},{scale}'
    }
    data = requests.get(URL, params=params).content
    return BytesIO(data)
