class Options:
    def __init__(self,name,quality,price,perAmount):
        self.name=name
        self.quality=quality
        self.price=price
        self.perAmount=perAmount


class IngredientsInfo:
    def __init__(self,name,groups,options):
        self.name=name
        self.groups=groups
        self.options=options


class Ingridients:
    def __init__(self,name,quantity,quantityType):
        self.name=name
        self.quantity=quantity
        self.quantityType=quantityType

class Meal:
    def __init__(self,id,name,ingredients):
        self.id=id
        self.name=name
        self.ingredients=ingredients

    


    