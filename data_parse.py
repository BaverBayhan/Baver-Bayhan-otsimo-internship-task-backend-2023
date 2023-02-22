from model_classes import Meal
from model_classes import Ingridients
from model_classes import Options
from model_classes import IngredientsInfo
import random
import json

json_raw_data=None
with open('data.json','r') as f:
  json_raw_data=json.load(f)

class Utils:
  meal_list_dict = json_raw_data["meals"]
  ingredients_info_list_dict = json_raw_data["ingredients"]
  
  def parse_meals(meal_list_dict):
    meal_obj_list = []
    for meal_data in meal_list_dict:
        ingredients_list = meal_data["ingredients"]
        ingredients_obj_list=[]
        for ingredient in ingredients_list:
            ingredient_obj= Ingridients(ingredient["name"],
                                        ingredient["quantity"],
                                        ingredient["quantity_type"])
            ingredients_obj_list.append(ingredient_obj)
        meal_obj= Meal(meal_data["id"],meal_data["name"],ingredients_obj_list)
        meal_obj_list.append(meal_obj)
    return meal_obj_list

  def parse_ingredients_info(ingredients_info_list_dict):
    ingredientsInfo_obj_list=[]
    for ingredients_info in ingredients_info_list_dict:
        options_list = ingredients_info["options"]
        option_obj_list=[]
        for option in options_list:
            option_obj = Options(option["name"],option["quality"],option["price"],option["per_amount"])
            option_obj_list.append(option_obj)
        ingredientInfo_obj=IngredientsInfo(ingredients_info["name"]
                                          ,ingredients_info["groups"]
                                          ,option_obj_list)
        ingredientsInfo_obj_list.append(ingredientInfo_obj)
    return ingredientsInfo_obj_list

  def list_meals(is_vegan,is_vegetarian):
      if(is_vegan):  
        vegan_meals_list=[]
        vegan_ingredients_list = []
        for ingredientInfo_obj in ingredientsInfo_obj_list:
            if('vegan' in ingredientInfo_obj.groups):
                vegan_ingredients_list.append(ingredientInfo_obj.name)
        for meal in meals_obj_list:
            flag=True
            for ingredient in meal.ingredients:
                if(ingredient.name not in vegan_ingredients_list):
                    flag=False
                    break
            if(flag):
                vegan_meals_list.append(meal)  
        return vegan_meals_list
      
      elif(is_vegetarian):
        vegetarian_meals_list=[]
        vegetarian_ingredients_list = []
        for ingredientInfo_obj in ingredientsInfo_obj_list:
            if('vegetarian' in ingredientInfo_obj.groups):
                vegetarian_ingredients_list.append(ingredientInfo_obj.name)
        for meal in meals_obj_list:
            flag=True
            for ingredient in meal.ingredients:
                if(ingredient.name not in vegetarian_ingredients_list):
                    flag=False
                    break
            if(flag):
                vegetarian_meals_list.append(meal)
            
        return vegetarian_meals_list
      else:
          return meals_obj_list
  
  def obj_to_dict(meals):
    meal_dicts = []
    for meal in meals:
        ingredient_dicts = [ingredient.__dict__ for ingredient in meal.ingredients]
        meal_dict = {
            'id': meal.id,
            'name': meal.name,
            'ingredients': ingredient_dicts
        }
        meal_dicts.append(meal_dict)
    return meal_dicts

  def get_meal_by_id(id):
    for meal in Utils.list_meals(False,False):
      if(meal.id==id):
        ingredient_info_list=[]
        for ingredient in meal.ingredients:
           for ingredient_info in Utils.ingredients_info_list_dict:
              if(ingredient.name==ingredient_info["name"]):
                ingredient_info_list.append(ingredient_info)
        meal_dict={
          'id':meal.id,
          'name':meal.name,
          'ingredients':ingredient_info_list
        }
        return meal_dict

  def calculate_quality_score(ingredients_names,params):
    quality_score=0
    for ingredient in ingredients_names:
      flag=True
      for k,v in params.items():
        if(ingredient==k):
          flag=False
          if(v[0]=='low'):
            quality_score+=10
          elif(v[0]=='medium'):
            quality_score+=20
          elif(v[0]=='high'):
             quality_score+=30
      if flag:
         quality_score+=30
    return quality_score/len(ingredients_names)
  
  def get_meal_option(quality_str,options):
    for option in options:
      if(option['quality']==quality_str):
        return option

  def get_modified_ingredients_list(meal_id,params):
    meal=None
    for M in meals_obj_list:
      if(M.id==meal_id):
        meal=M
        break
    ingredients_list=[]
    for ingredient in meal.ingredients:
      ingredients_list.append(ingredient.__dict__)
    ingredients_info_list=[]
    meal_with_ingredients_infos=Utils.get_meal_by_id(meal_id)
    for ingredient_info in meal_with_ingredients_infos['ingredients']:
      ingredients_info_list.append(ingredient_info)
    ingredient_options_list=[]
    for ingredient in ingredients_info_list:
      flag=True
      for key,value in params.items():
        if ingredient['name']==key:
          ingredient_options_list.append(Utils.get_meal_option(value[0],ingredient['options']))
          flag=False
      if flag:
        ingredient_options_list.append(Utils.get_meal_option('high',ingredient['options']))
    for i in range(len(ingredients_list)):
      ingredients_list[i]['price']= ingredient_options_list[i]['price']
      ingredients_list[i]['quality']=ingredient_options_list[i]['quality']
    return ingredients_list
  
  def calculate_price(meal_id,params):
    modified_ingredients_list=Utils.get_modified_ingredients_list(meal_id,params)
    price_of_meal=0
    for ingredient in modified_ingredients_list:
      price_of_meal+=(ingredient['quantity']/1000)*ingredient['price']
      if(ingredient['quality']=='low'):
        price_of_meal+=0.10
      elif(ingredient['quality']=='medium'):
        price_of_meal+=0.05
    return price_of_meal

  def update_helper_list(helper_list):
    return sorted(helper_list*3)
  
  def generate_params_list(params_list):
    value_list=[]
    for elem in params_list:
      value_list.append(list(elem.values()))

    helper_list=[0,1,2]
    speed=3
    for i in range(len(value_list[0])):
      k=len(value_list[0])-i-1
      for j in range(len(value_list)):
        value_list[j][k]+=helper_list[j%speed]
      helper_list=Utils.update_helper_list(helper_list)
      speed*=3
    for i in range(len(value_list[0])):
      k=len(value_list[0])-i-1
      for j in range(len(value_list)):
        if(value_list[j][i]==1):
          value_list[j][i]='low'
        elif(value_list[j][i]==2):
          value_list[j][i]='medium'
        elif(value_list[j][i]==3):
          value_list[j][i]='high'

    return value_list
          
  def generate_possible_ingredients(meal_id):
    meal=None
    for M in Utils.meal_list_dict:
      if(M['id']==meal_id):
        meal=M
    params_list = []
    for it in range(3**len(meal['ingredients'])):
      param={}
      for ing in meal['ingredients']:
        param[ing['name']]=1
      params_list.append(param)

    qualities_list=Utils.generate_params_list(params_list)
    
    for i in range(len(qualities_list)):
      dict1=params_list[i]
      list1=qualities_list[i]
      keys = list(dict1.keys())  
      for i, key in enumerate(keys):
        dict1[key] = list1[i]
    for params in params_list:
      for k,v in params.items():
        params[k]=[v]
    return params_list
  
  def get_shortened_ingredients_list(ingredient):
    shortened_ingredients_list=[]
    for key,value in ingredient.items():
      name_of_specific_ingredient=None
      for ingredient_info in Utils.ingredients_info_list_dict:
        if(key==ingredient_info['name']):
           for option in ingredient_info['options']:
              if(option['quality']==value[0]):
                name_of_specific_ingredient=option['name']
      dict_={
        'name':name_of_specific_ingredient,
        'quality':value[0]       
      }
      shortened_ingredients_list.append(dict_)
    return shortened_ingredients_list

  def generate_versions_of_meal(meal_id):
    name=Utils.get_meal_by_id(meal_id)['name']
    possible_ingredients=Utils.generate_possible_ingredients(meal_id)
    versions_list=[]
    for ingredient in possible_ingredients:
      price=format(Utils.calculate_price(meal_id,ingredient),'.2f')
      quality=format(Utils.calculate_quality_score(list(ingredient.keys()),ingredient),'.1f')
      shortened_ingredients_list=Utils.get_shortened_ingredients_list(ingredient)
      _dict={
        'id':meal_id,
        'name':name,
        'price':price,
        'quality_score':quality,
        'ingredients':shortened_ingredients_list
      }
      versions_list.append(_dict)
    return versions_list

  def all_possible_meals(all_meal_ids):
    all_possible_meals_list=[]
    for meal_id in all_meal_ids:
      possible_meals=Utils.generate_versions_of_meal(meal_id)
      for meal in possible_meals:
        all_possible_meals_list.append(meal)
    return all_possible_meals_list

  def feeling_lucky_impl(all_meal_ids,budget):
    all_possible_meals_list=Utils.all_possible_meals(all_meal_ids)
    filtered_meals=[]
    for meal in all_possible_meals_list:
      if(budget>float(meal['price']) or budget==float(meal['price'])):
        filtered_meals.append(meal)
    rand_num=random.randint(0,len(filtered_meals)-1)
    return filtered_meals[rand_num]
    
  def keyword_search(query):
    for meal in Utils.meal_list_dict:
      if(query.lower() in meal['name'].lower()):
        ingredients=[]
        for ingredient in meal['ingredients']:
          ingredients.append(ingredient['name'])
        return {
          'id':meal['id'],
          'name':meal['name'],
          'ingredients':ingredients
        }
    return None
    
  def find_heighest_quality(budget,is_vegetarian,is_vegan):
    final_meal=None
    filtered_meals=Utils.list_meals(is_vegetarian,is_vegan)
    quality=0
    meal_ids=[]
    for meal in filtered_meals:
      meal_ids.append(meal.id)
    possible_meals=Utils.all_possible_meals(meal_ids)
    for filter_meal in possible_meals:
      if(budget>float(filter_meal['price']) or budget==float(filter_meal['price'])):
        if(float(filter_meal['quality_score'])>quality):
          quality=float(filter_meal['quality_score'])
          final_meal=filter_meal
    return final_meal
        
  def find_heighst_quality_version(meal_id,budget):
    final_meal=None
    versions_of_meal_list=Utils.generate_versions_of_meal(meal_id)
    quality=0
    for version in versions_of_meal_list:
      if(budget>float(version['price']) or budget==float(version['price'])):
        if(float(version['quality_score'])>quality):
          quality=float(version['quality_score'])
          final_meal=version
    return final_meal


      


ingredientsInfo_obj_list=Utils.parse_ingredients_info(Utils.ingredients_info_list_dict)

meals_obj_list=Utils.parse_meals(Utils.meal_list_dict)

meals_list = Utils.list_meals(False,False)




     










