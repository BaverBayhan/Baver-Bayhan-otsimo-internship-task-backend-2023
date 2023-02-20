from data_parse import meals_obj_list
from data_parse import ingredientsInfo_obj_list
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

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
        if parsed_url.path == '/listMeals':
            meals = get_meals(is_vegetarian, is_vegan)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(meals).encode())
        else:
            self.send_error(404)



def get_meals(is_vegetarian, is_vegan):
    if is_vegan == True:
        vegan_meals_list=[]
        vegan_ingredients_list = []
        for ingredientInfo_obj in ingredientsInfo_obj_list:
            if('vegan' in ingredientInfo_obj.groups):
                vegan_ingredients_list.append(ingredientInfo_obj.name)
        for meal in meals_obj_list:
            flag=True
            for ingredient in meal.ingredients:
                if(ingredient.name not in vegan_meals_list):
                    flag=False
            if(flag):
                vegan_meals_list.append(meal)
            
            
    




if __name__ == '__main__':
    # Start the web server on port 8080
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Server running on port 8080...')
    httpd.serve_forever()


    
