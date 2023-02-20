class Options:
    def __init__(self,name,quality,price,perAmount):
        self._name=name
        self._quality=quality
        self._price=price
        self._perAmount=perAmount
    @property
    def name(self):
        return self._name
    @property
    def quality(self):
        return self._name
    @property
    def price(self):
        return self._name
    @property
    def perAmount(self):
        return self._perAmount

class IngredientsInfo:
    def __init__(self,name,groups,options):
        self._name=name
        self._groups=groups
        self._options=options
    @property
    def name(self):
        return self._name
    @property
    def groups(self):
        return self._groups
    @property
    def options(self):
        return self._options

class Ingridients:
    def __init__(self,name,quantity,quantityType):
        self._name=name
        self._quantity=quantity
        self._quantityType=quantityType
    @property
    def name(self):
        return self._name
    @property
    def quantity(self):
        return self._quantity
    @property
    def quantityType(self):
        return self._quantityType

class Meal:
    def __init__(self,id,name,ingredients):
        self._id=id
        self._name=name
        self._ingredients=ingredients
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def ingredients(self):
        return self._ingredients

    


    