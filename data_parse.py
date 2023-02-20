from model_classes import Meal
from model_classes import Ingridients
from model_classes import Options
from model_classes import IngredientsInfo

json_raw_data ={
  "meals": [
    {
      "id": 1,
      "name": "Rice and chicken bowl",
      "ingredients": [
        { "name": "Rice", "quantity": 120, "quantity_type": "gram" },
        { "name": "Chicken", "quantity": 85, "quantity_type": "gram" }
      ]
    },
    {
      "id": 2,
      "name": "Pasta with marinara sauce and vegetables",
      "ingredients": [
        { "name": "Pasta", "quantity": 115, "quantity_type": "gram" },
        {
          "name": "Marinara sauce",
          "quantity": 120,
          "quantity_type": "millilitre"
        },
        { "name": "Vegetables", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 3,
      "name": "Grilled chicken with roasted vegetables",
      "ingredients": [
        { "name": "Chicken", "quantity": 85, "quantity_type": "gram" },
        { "name": "Vegetables", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 4,
      "name": "Beef stir-fry with rice",
      "ingredients": [
        { "name": "Beef", "quantity": 115, "quantity_type": "gram" },
        { "name": "Rice", "quantity": 120, "quantity_type": "gram" },
        { "name": "Vegetables", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 5,
      "name": "Pork chops with mashed potatoes and gravy",
      "ingredients": [
        { "name": "Pork chops", "quantity": 115, "quantity_type": "gram" },
        {
          "name": "Mashed potatoes",
          "quantity": 120,
          "quantity_type": "gram"
        },
        { "name": "Gravy", "quantity": 120, "quantity_type": "millilitre" }
      ]
    },
    {
      "id": 6,
      "name": "Grilled salmon with roasted asparagus",
      "ingredients": [
        { "name": "Salmon", "quantity": 85, "quantity_type": "gram" },
        { "name": "Asparagus", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 7,
      "name": "Shrimp scampi with linguine",
      "ingredients": [
        { "name": "Shrimp", "quantity": 115, "quantity_type": "gram" },
        { "name": "Linguine", "quantity": 115, "quantity_type": "gram" },
        { "name": "Butter", "quantity": 10, "quantity_type": "millilitre" },
        { "name": "Garlic", "quantity": 10, "quantity_type": "gram" },
        { "name": "White wine", "quantity": 60, "quantity_type": "millilitre" }
      ]
    },
    {
      "id": 8,
      "name": "Vegetarian stir-fry with tofu",
      "ingredients": [
        { "name": "Tofu", "quantity": 115, "quantity_type": "gram" },
        { "name": "Rice", "quantity": 120, "quantity_type": "gram" },
        { "name": "Vegetables", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 9,
      "name": "Fruit salad with mixed berries and yogurt",
      "ingredients": [
        { "name": "Mixed berries", "quantity": 240, "quantity_type": "gram" },
        { "name": "Yogurt", "quantity": 120, "quantity_type": "millilitre" }
      ]
    }
  ],

  "ingredients": [
    {
      "name": "Rice",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Long grain white rice",
          "quality": "high",
          "price": 3,
          "per_amount": "kilogram"
        },
        {
          "name": "Medium grain brown rice",
          "quality": "medium",
          "price": 2,
          "per_amount": "kilogram"
        },
        {
          "name": "Quick cooking white rice",
          "quality": "low",
          "price": 1.5,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Pasta",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "Semolina pasta",
          "quality": "high",
          "price": 2,
          "per_amount": "kilogram"
        },
        {
          "name": "Whole wheat pasta",
          "quality": "medium",
          "price": 1.5,
          "per_amount": "kilogram"
        },
        {
          "name": "Enriched pasta",
          "quality": "low",
          "price": 1,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Chicken",
      "groups": [],
      "options": [
        {
          "name": "Organic, free-range chicken",
          "quality": "high",
          "price": 10,
          "per_amount": "kilogram"
        },
        {
          "name": "Conventional chicken",
          "quality": "medium",
          "price": 7,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen chicken",
          "quality": "low",
          "price": 4,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Beef",
      "groups": [],
      "options": [
        {
          "name": "Grass-fed beef",
          "quality": "high",
          "price": 16,
          "per_amount": "kilogram"
        },
        {
          "name": "Grain-fed beef",
          "quality": "medium",
          "price": 12,
          "per_amount": "kilogram"
        },
        {
          "name": "Processed beef",
          "quality": "low",
          "price": 8,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Pork",
      "groups": [],
      "options": [
        {
          "name": "Heritage breed pork",
          "quality": "high",
          "price": 12,
          "per_amount": "kilogram"
        },
        {
          "name": "Conventional pork",
          "quality": "medium",
          "price": 9,
          "per_amount": "kilogram"
        },
        {
          "name": "Processed pork",
          "quality": "low",
          "price": 6,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Salmon",
      "groups": [],
      "options": [
        {
          "name": "Wild-caught salmon",
          "quality": "high",
          "price": 24,
          "per_amount": "kilogram"
        },
        {
          "name": "Farmed salmon",
          "quality": "medium",
          "price": 16,
          "per_amount": "kilogram"
        },
        {
          "name": "Canned tuna",
          "quality": "low",
          "price": 8,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Shrimp",
      "groups": [],
      "options": [
        {
          "name": "Wild-caught shrimp",
          "quality": "high",
          "price": 20,
          "per_amount": "kilogram"
        },
        {
          "name": "Farm-raised shrimp",
          "quality": "medium",
          "price": 15,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen shrimp",
          "quality": "low",
          "price": 10,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Vegetables",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic vegetables",
          "quality": "high",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional vegetables",
          "quality": "medium",
          "price": 5,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen vegetables",
          "quality": "low",
          "price": 3,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Fruit",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic fruit",
          "quality": "high",
          "price": 6,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional fruit",
          "quality": "medium",
          "price": 4,
          "per_amount": "kilogram"
        },
        {
          "name": "Canned fruit",
          "quality": "low",
          "price": 2,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Dairy",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "Organic, grass-fed dairy",
          "quality": "high",
          "price": 16,
          "per_amount": "litre"
        },
        {
          "name": "Conventional dairy",
          "quality": "medium",
          "price": 8,
          "per_amount": "litre"
        },
        {
          "name": "Processed dairy",
          "quality": "low",
          "price": 4,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Marinara sauce",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Homemade marinara sauce",
          "quality": "high",
          "price": 20,
          "per_amount": "litre"
        },
        {
          "name": "Store-bought marinara sauce",
          "quality": "medium",
          "price": 12,
          "per_amount": "litre"
        },
        {
          "name": "Canned marinara sauce",
          "quality": "low",
          "price": 6,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Butter",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "Grass-fed butter",
          "quality": "high",
          "price": 12,
          "per_amount": "kilogram"
        },
        {
          "name": "Conventional butter",
          "quality": "medium",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Margarine",
          "quality": "low",
          "price": 4,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Garlic",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic garlic",
          "quality": "high",
          "price": 6,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional garlic",
          "quality": "medium",
          "price": 4,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen garlic",
          "quality": "low",
          "price": 2,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "White wine",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "High-end white wine",
          "quality": "high",
          "price": 40,
          "per_amount": "litre"
        },
        {
          "name": "Mid-range white wine",
          "quality": "medium",
          "price": 30,
          "per_amount": "litre"
        },
        {
          "name": "Cheap white wine",
          "quality": "low",
          "price": 20,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Mashed potatoes",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Homemade mashed potatoes",
          "quality": "high",
          "price": 10,
          "per_amount": "litre"
        },
        {
          "name": "Store-bought mashed potatoes",
          "quality": "medium",
          "price": 7,
          "per_amount": "litre"
        },
        {
          "name": "Instant mashed potatoes",
          "quality": "low",
          "price": 4,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Gravy",
      "groups": [],
      "options": [
        {
          "name": "Homemade gravy",
          "quality": "high",
          "price": 10,
          "per_amount": "litre"
        },
        {
          "name": "Store-bought gravy",
          "quality": "medium",
          "price": 7,
          "per_amount": "litre"
        },
        {
          "name": "Instant gravy",
          "quality": "low",
          "price": 4,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Asparagus",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic asparagus",
          "quality": "high",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional asparagus",
          "quality": "medium",
          "price": 5,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen asparagus",
          "quality": "low",
          "price": 3,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Tofu",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "High-quality tofu",
          "quality": "high",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Medium-quality tofu",
          "quality": "medium",
          "price": 6,
          "per_amount": "kilogram"
        },
        {
          "name": "Low-quality tofu",
          "quality": "low",
          "price": 4,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Yogurt",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "Organic, grass-fed yogurt",
          "quality": "high",
          "price": 12,
          "per_amount": "litre"
        },
        {
          "name": "Conventional yogurt",
          "quality": "medium",
          "price": 8,
          "per_amount": "litre"
        },
        {
          "name": "Processed yogurt",
          "quality": "low",
          "price": 4,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Mixed berries",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic mixed berries",
          "quality": "high",
          "price": 12,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional mixed berries",
          "quality": "medium",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen mixed berries",
          "quality": "low",
          "price": 4,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Linguine",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "High-end linguine",
          "quality": "high",
          "price": 2,
          "per_amount": "kilogram"
        },
        {
          "name": "Mid-range linguine",
          "quality": "medium",
          "price": 1.5,
          "per_amount": "kilogram"
        },
        {
          "name": "Cheap linguine",
          "quality": "low",
          "price": 1,
          "per_amount": "kilogram"
        }
      ]
    }
  ]
}

meal_list_dict = json_raw_data["meals"]
ingredients_info_list_dict = json_raw_data["ingredients"]

class Utils:
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
    dict_list = []
    for meal in meals:
      meal_dict=meal.__dict__
      for ingredient in meal_dict["_ingredients"]:
        meal_dict["_ingredients"]=ingredient.__dict__
      dict_list.append(meal_dict)
    return dict_list

ingredientsInfo_obj_list=Utils.parse_ingredients_info(ingredients_info_list_dict)
meals_obj_list=Utils.parse_meals(meal_list_dict)



meals_list = Utils.list_meals(False,False)

            


dict_list = Utils.obj_to_dict(meals_list)

for i in dict_list:
    print(i,"\n")

       





