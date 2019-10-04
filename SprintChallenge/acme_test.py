import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    '''Making sure Acme products are the tops!'''
    def test_default_product_price(self):
        '''Test default product price is 10.'''
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        '''Test default product weight is 20.'''
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    
    def test_stealability(self):
        '''Test stealability when product price is 30.'''
        pro = Product(price=30)
        self.assertEqual(pro.stealability(), 'Very Stealable')

class AcmeReportTests(unittest.TestCase):
    '''Tests that components of reports are functional.'''

    def test_default_num_products(self):
        '''Test default num_products is 30.'''
        gn = generate_products()
        self.assertEqual(len(gn), 30)
    
    def test_legal_names(self):
        '''Tests that product names are actually.'''
        gn = generate_products()
        nouns =set()
        adj = set()

        for product in gn:
            nouns.add(product.name.split()[1])
            adj.add(product.name.split()[0])

        nouns = list(nouns)
        adj = list(adj)

        self.assertIn(nouns, NOUNS)
        self.assertIn(adj, ADJECTIVES)






if __name__ == '__main__':
    unittest.main()