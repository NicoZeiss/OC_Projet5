# -*- coding: Utf-8 -*-

'''Here are all the 3 classes we use in our program'''

import requests
from constants import api_url, product_url, cat_url, cat_size


class Product(object):
    '''One instance of Product represent one product from openfoodfacts'''

    def __init__(self, barcode, cat_id):
        self.code = barcode
        self.api_url = api_url + barcode +'.json'
        self.url = product_url + barcode
        self.product = {"code": "", "name": "", "store": "", "cat_id": "", "grade": "", "product_url": ""}
        self.cat_id = cat_id

    def create_prod(self):
        '''we extract informations from API'''

        request = requests.get(self.api_url).json()
        self.product['code'] = self.code
        self.product['name'] = request['product']['product_name']
        stores = request['product']['stores'].split(",")
        self.product['store'] = stores[0]
        self.product['cat_id'] = self.cat_id
        self.product['grade'] = request['product']['nutrition_grade_fr']
        self.product['product_url'] = self.url

    def save_prod(self, mycursor, mydb):
        '''we insert datas into DB'''

        request = "INSERT INTO Products (code, name, store, cat_id, grade, product_url) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.product["code"], self.product["name"], self.product["store"], self.product["cat_id"], self.product["grade"], self.product["product_url"])
        mycursor.execute(request, val)
        mydb.commit()


class Category(object):
    '''One category contain bar code of all its products into a list'''

    def __init__(self, cat_name):
        self.name = cat_name
        self.cat_url = cat_url + cat_name + "/"
        self.product_list = []

    def create_product_list(self):
        '''we append the list'''

        i = 1
        while i != 0:
            cat = requests.get(self.cat_url + str(i) + '.json').json()
            if len(cat["products"]) != 0:
                for j in range(0, len(cat["products"])):
                    code = cat['products'][j]['code']
                    request = requests.get(api_url + code + '.json').json()
                    if 'nutrition_grade_fr' in request['product'] and 'stores' in request['product']:
                        if request['product']['stores'] != "":
                            if len(self.product_list) < cat_size:
                                self.product_list.append(code)
                            else:
                                i = -1
                                break
            else:
                break
            i += 1

    def insert_into_db(self, mycursor, mydb):
        '''we insert datas into DB'''

        request = "INSERT INTO Categories (name) VALUES (%s)"
        val = (self.name,)
        mycursor.execute(request, val)
        mydb.commit()


class Substitute(object):
    '''with this class we'll save substitutes in our DB'''

    def __init__(self, subs, prod):
        self.prod_id = prod
        self.subs_id = subs

    def add_to_db(self, mycursor, mydb):
        '''we insert prod and subs id in our db, table Favorites'''

        request = "INSERT INTO Favorites (prod_id, subs_id) VALUES (%s, %s)"
        val = (self.prod_id, self.subs_id)
        mycursor.execute(request, val)
        mydb.commit()
