from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        # print('url.components', url_components)
        query_string_list = parse.parse_qsl(url_components.query)
        # print("query.string.list", query_string_list)
        dic = dict(query_string_list)
        capital = dic.get('capital')
        country = dic.get('country')

        if capital:
            capital_url = f"https://restcountries.com/v3.1/capital/{capital}"
            r = requests.get(capital_url)
            data = r.json()
            definitions = []
            for capital_data in data:
                country = capital_data[0]['capital'][0]
                print(country)
                definitions.append(country)
            message = str(definitions)
        elif country:
            country_url = f'https://restcountries.com/v3.1/name/{country}'
            r = requests.get(country_url)
            data = r.json()
            definitions = []
            for country_data in data:
                capital_name = country_data[0]['capital'][0]
                definitions.apped(capital_name)
            message = str(definitions)
        else:
            message = "Give me a city name please"
        # message = "test message"
        print(message)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return



