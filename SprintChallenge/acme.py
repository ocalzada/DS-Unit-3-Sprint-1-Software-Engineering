from random import randint

class Product:
    '''
    Product - is a good sold and managed by the Acme Corporation.
    ----------------------------
    name: str
    price: int
    weight: int
    flammability: float
    identifier: int (value will vary)
    '''
    def __init__(self, name=None, price=10, weight=20, flammability=0.5, identifier=randint(1000000, 9999999)):
        self.name = name 
        self.price = price
        self.weight = weight 
        self.flammability = flammability
        self.identifier = identifier
    
    def stealability(self):
        '''
        This function explains how stealable (or not) a product is.
        '''
        ratio = self.price/self.weight
        if ratio < 0.5: 
            return 'Not so stealable'
        elif ratio >= 0.5 and ratio < 1.0: 
            return 'Kinda Stealable'
        else:
            return 'Very Stealable'

    def explode(self):
        '''
        This function describes whether a product will explode.
        '''
        fw = self.flammability * self.weight
        if fw < 10:
            return '...fizzle'
        elif fw >= 10 and fw < 50:
            return '...boom!'
        else:
            return '...BABOOM'

class BoxingGlove(Product):
    '''
    BoxingGlove - is a specific type of Product sold and managed by the Acme Corporation.
    '''
    def __init__(self, name=None, price=10, weight=10, flammability=0.5, identifier=randint(1000000, 9999999)):
        super().__init__(name=name, price=price, weight=weight, flammability=flammability, identifier=identifier)

    def explode(self):
        '''
        explode - is subclass function that overrides the Parent class
        and clarifies or reiterates that the product is a glove.
        '''
        return '...it is a glove'
    
    def punch(self):
        '''
        punch - is also a subclass function that explains how much a punch
        will hurt given its weight.
        '''
        weight = self.weight
        if weight < 5:
            return 'That tickles.'
        elif weight >= 5 and weight < 15:
            return 'Hey that hurt'
        else:
            return 'OUCH'



    