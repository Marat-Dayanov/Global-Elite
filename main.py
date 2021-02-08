import os
import sys

import pygame
import requests

map_request = "http://static-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b"
response = requests.get(map_request)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_coodrinates = toponym["Point"]["pos"]
    print(toponym_address, "имеет координаты:", toponym_coodrinates)
else:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
