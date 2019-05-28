from rest_server import start_restful_server
import json


if __name__ == '__main__':
    settings: dict
    with open("settings.json", 'r') as settings_file:
        settings = json.load(settings_file)
    host = settings.get('host')
    port = int(settings.get('port'))

    start_restful_server()
