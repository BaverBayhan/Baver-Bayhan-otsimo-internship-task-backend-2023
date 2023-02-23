from data_parse import Utils
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

class RestaurantAPIRequestHandler(BaseHTTPRequestHandler):
    

    def do_GET(self):
        error_body={
            'statusCode':404,
            'error':'Not found'
        }
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
            if meal is not None:
                response_json=json.dumps(meal)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response_json.encode())
            else:
                error_body['message']='Meal not found'
                response_json = json.dumps(error_body)
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response_json.encode())

        elif parsed_url.path=='/search':
            params=parse_qs(parsed_url.query)
            meal=Utils.keyword_search(params['query'][0])
            if meal is not None:
                response=json.dumps(meal)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response.encode())
            else:
                error_body['message']='No meal found with given keyword'
                response_json = json.dumps(error_body)
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response_json.encode())

    def do_POST(self):
        parsed_url = urlparse(self.path)
        error_body={
            'statusCode':404,
            'error':'Not found'
        }

        if parsed_url.path == '/quality':
            params = parse_qs(parsed_url.query)
            meal = Utils.get_meal_by_id(int(params['meal_id'][0]))
            if meal is not None:
                meal_ingredients=meal['ingredients']
                ingredients_names=[]
                for ing in meal_ingredients:
                    ingredients_names.append(ing['name'])
                quality_score=float(format(Utils.calculate_quality_score(ingredients_names,params),'.1f'))
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {'quality': quality_score}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                error_body['message']='No meal found with given keyword'
                response_json = json.dumps(error_body)
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response_json.encode())


        elif parsed_url.path=='/price':
            params = parse_qs(parsed_url.query)
            meal_ids_list=[]
            for i in Utils.meal_list_dict:
                meal_ids_list.append(i['id'])
            if int(params['meal_id'][0]) in meal_ids_list:
                price = float(format(Utils.calculate_price(int(params['meal_id'][0]),params),'.2f'))
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {'price': price}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                error_body['message']='Meal not found (Invalid meal id)'
                response_json = json.dumps(error_body)
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response_json.encode())

        elif parsed_url.path=='/random':
            params=parse_qs(parsed_url.query)
            meal_ids_list=[]
            for i in Utils.meal_list_dict:
                meal_ids_list.append(i['id'])
            price=float('inf')
            if 'budget' in params:
                price=float(params['budget'][0])
            response=Utils.feeling_lucky_impl(meal_ids_list,price)
            if response is not None:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                error_body['message']='Meal not found (Low budget)'
                response_json = json.dumps(error_body)
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response_json.encode())

        elif parsed_url.path=='/findHeighest':
            params=parse_qs(parsed_url.query)
            is_vegetarian='false'
            is_vegan='false'
            if 'is_vegetarian' in params:
                is_vegetarian=params['is_vegetarian'][0]
            if 'is_vegan' in params:
                is_vegan=params['is_vegan'][0]
            meal=Utils.find_heighest_quality(
                float(params['budget'][0]),
                is_vegetarian=='true',
                is_vegan=='true')
            if meal is not None:
                response=json.dumps(meal)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(response.encode('utf-8'))
            else:
                error_body['message']='Meal not found (No meal matching with given parameters)'
                response_json = json.dumps(error_body)
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response_json.encode())

        elif parsed_url.path=='/findHighestOfMeal':
            params=parse_qs(parsed_url.query)
            meal=Utils.find_heighest_quality_version(
                int(params['meal_id'][0]),
                float(params['budget'][0]),
            )
            if meal is not None:
                response=json.dumps(meal)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(response.encode('utf-8'))    
            else:
                error_body['message']='Meal not found (No meal matching with given parameters)'
                response_json = json.dumps(error_body)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(response_json.encode('utf-8'))    

            

if __name__ == '__main__':
    # Start the web server on port 8080
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RestaurantAPIRequestHandler)
    print('Server running on port 8080...')
    httpd.serve_forever()