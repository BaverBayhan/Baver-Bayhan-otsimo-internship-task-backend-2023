from data_parse import Utils
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        is_vegetarian = False
        if 'is_vegetarian' in query_params:
            is_vegetarian = query_params['is_vegetarian'][0].lower() == 'true'
        is_vegan = False
        if 'is_vegan' in query_params:
            is_vegan = query_params['is_vegan'][0].lower() == 'true'

        # Process the request based on the path and query parameters
        if parsed_url.path == '/listMeals':
            # Return a list of meals based on the query parameters
            meals = Utils.list_meals(is_vegetarian, is_vegan)
            dict_list=Utils.obj_to_dict(meals)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(dict_list.encode())
        else:
            # Return a 404 error for any other path
            self.send_error(404)
