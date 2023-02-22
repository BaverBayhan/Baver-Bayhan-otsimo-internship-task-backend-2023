from data_parse import Utils
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

class RestaurantAPIRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query=parse_qs(parsed_url.query)

        if parsed_url.path == '/listMeals':
            params = parse_qs(parsed_url.query)
            is_vegan = params.get('is_vegan', ['false'])[0] == 'true'
            is_vegetarian = params.get('is_vegetarian', ['false'])[0] == 'true'
            filtered_meal = Utils.list_meals(is_vegan,is_vegetarian)
            dicts_list = Utils.obj_to_dict(filtered_meal)
            response_json = json.dumps(dicts_list)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response_json.encode())

        elif parsed_url.path == '/getMeal':
            meal_id = int(query.get('id', [None])[0])
            meal=Utils.get_meal_by_id(meal_id)
            response_json=json.dumps(meal)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response_json.encode())

    def do_POST(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path == '/quality':
            params = parse_qs(parsed_url.query)
            meal_ingredients = Utils.get_meal_by_id(int(params['meal_id'][0]))['ingredients']
            ingredients_names=[]
            for ing in meal_ingredients:
                ingredients_names.append(ing['name'])
            quality_score=Utils.calculate_quality_score(ingredients_names,params)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {'quality': quality_score}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        elif parsed_url.path=='/price':
            params = parse_qs(parsed_url.query)
            price = Utils.calculate_price(int(params['meal_id'][0]),params)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {'price': price}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        elif parsed_url.path=='/random':
            params=parse_qs(parsed_url.query)
            meal_ids_list=[]
            for i in Utils.meal_list_dict:
                meal_ids_list.append(i['id'])
            response=Utils.feeling_lucky_impl(meal_ids_list,float(params['budget'][0]))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
            



    




            




if __name__ == '__main__':
    # Start the web server on port 8080
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RestaurantAPIRequestHandler)
    print('Server running on port 8080...')
    httpd.serve_forever()