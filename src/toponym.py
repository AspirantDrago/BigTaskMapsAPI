import dataclasses

import requests

from .secrets import API_KEY_GEOCODER

API_URL_GEOCODER = 'https://geocode-maps.yandex.ru/1.x'


@dataclasses.dataclass
class Toponym:
    longitude: float
    latitude: float
    search_text: str

    @classmethod
    def from_search_text(cls, search_text: str):
        response = requests.get(API_URL_GEOCODER, params={
            'apikey': API_KEY_GEOCODER,
            'geocode': search_text,
            'format': 'json',
            'results': 1
        })
        if not response:
            return None
        json_data = response.json()['response']
        geo_obj = json_data['GeoObjectCollection']['featureMember'][0]['GeoObject']
        long, lat = map(float, geo_obj['Point']['pos'].split())

        return cls(longitude=long, latitude=lat, search_text=search_text)
