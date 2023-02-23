# Otsimo Backend Internship Task

In this repo I have created Transparent Restaurant Backend REST api. All endpoints including bonusses has been implemented. URLs, HTTP methods and
parameters are below.

To test the api put the data in "data.json" (default content of file is the dataset in Gist task) and run  API.py file . Server will start in http://localhost:8080

<-- ! --> There is a typo in the original dataset in Gist. The "Pork Chops" mentioned in the ingredients list of meal with id 5 is listed as "Pork" in the ingredients list below of meals. So, I changed "Pork Chops" to "Pork" in the ingredients list below meals.

***********************************************************
PATH: /listMeals
METHOD: GET
PARAMS:
  is_vegetarian: (boolean, optional) default=false
  is_vegan: (boolean, optional) default=false
 
(Lists the menu according to vegan and vegetarian filters)
***********************************************************
PATH: /getMeal
METHOD: GET
PARAMS:
    id: N (integer, required)

(Gets the meal by id) 
***********************************************************
PATH: /quality
METHOD: POST
PARAMS:
  meal_id: (integer, required)
  <ingredient-1>: (enum, values: ["high", "medium", "low"], optional) default="high"
  <ingredient-2>: (enum, values: ["high", "medium", "low"], optional) default="high"
  ...

(calculates quality of a meal with given parameters)

***********************************************************
PATH: /price
METHOD: POST
PARAMS:
  meal_id: (integer, required)
  <ingredient-1>: (enum, values: ["high", "medium", "low"], optional) default="high"
  <ingredient-2>: (enum, values: ["high", "medium", "low"], optional) default="high"
  ...

(calculates price of a meal with given parameters)

***********************************************************
PATH: /random
METHOD: POST
PARAMS:
  budget: (double, optional) default=unlimited
  
(provides a random meal with given budget parameter.)

***********************************************************
PATH: /search
METHOD: GET
PARAMS:
  query: (string, required)
  
 (keyword search functionality)

***********************************************************
PATH: /findHighest
METHOD: POST
PARAMS:
  budget: (double, required)
  is_vegetarian: (boolean, optional) default=false
  is_vegan: (boolean, optional) default=false

(takes a budget as input and yields the highest-quality meal that can be
prepared for that budget and how much it costs.)

***********************************************************
PATH: /findHighestOfMeal
METHOD: POST
PARAMS:
  meal_id: (integer, required)
  budget: (double, required)

(takes a budget and meal id as input and yields the highest-quality version
of it that can be prepared for that budget and how much it costs.)


***********************************************************






