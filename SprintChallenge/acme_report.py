from acme import Product
from random import randint, sample, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    '''
    generate products - function to randomly generate a list of products.
    '''
    products = []

    for _ in list(range(num_products)):
        product_names = sample(ADJECTIVES,1)+sample(NOUNS,1)
        product = Product(name = ''.join(product_names),
                        price=randint(5, 100), weight=randint(5,100),
                        flammability=uniform(0.0, 2.5))
        products.append(product)
    return products

def inventory_report(products):
    '''
    Inventory Report - prints out an Inventory Report of Products
    for the Acme Corporation.
    products: list
    '''
    #baseline totals

    price_total = 0
    weight_total = 0
    flammability_total = 0

    names = set()
    for product in products:
        names.add(product.name)
        price_total += product.price
        weight_total += product.weight
        flammability_total += product.flammability
    
    price_avg = price_total/len(products)
    weight_avg = weight_total/len(products)
    flammability_avg = flammability_total/len(products)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', len(names))
    print('Average price:', price_avg)
    print('Average weight:', weight_avg)
    print('Average flammability:', flammability_avg)
    
if __name__ == '__main__':
    inventory_report(generate_products())    