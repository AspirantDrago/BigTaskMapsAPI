from io import BytesIO

import requests

from .map_config import Map
from .secrets import STATIC_MAPS_API


def get_image(map_config: Map) -> BytesIO:
    URL = 'https://static-maps.yandex.ru/v1'
    params = {
        'apikey': STATIC_MAPS_API,
        'll': f'{map_config.longitude},{map_config.latitude}',
        'spn': f'{map_config.scale},{map_config.scale}',
        'theme': 'dark' if map_config.dark_theme else 'light',
    }
    data = requests.get(URL, params=params).content
    return BytesIO(data)
