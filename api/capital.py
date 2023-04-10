from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        print('url.components', url_components)
        query_string_list = parse.parse_qsl(url_components.query)
        print("query.string.list", query_string_list)
        dic = dict(query_string_list)
        #
        # if capital in dic:
        #     url = f"https://restcountries.com/v3.1/capital/{capital}"
        #     r = requests.get(url + dic["word"])
        #     data = r.json()
        #     definitions = []
        #     for word_data in data:
        #         definition = word_data["meanings"][0]["definitions"][0]["definition"]
        #         definitions.append(definition)
        #     message = str(definitions)
        #
        # else:
        #     message = "Give me a city name please"
        message = "test message"
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return



