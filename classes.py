# -*- coding: Utf-8 -*-

'''Here are all the 3 classes we use in our program'''

import requests
from constants import api_url, product_url, cat_url, cat_size


class Product(object):
    '''One instance of Product represent one product from openfoodfacts'''

    def __init__(self):
        self.name = ""
        self.grade = ""
        self.store = ""
        self.url = ""
        self.cat_id = 0

    def create_prod(self,p_name, p_grade, p_store, p_url, p_catid, mycursor):
        '''we extract informations from API'''

        self.name = p_name
        self.grade = p_grade
        self.store = p_store
        self.url = p_url
        self.cat_id = p_catid

        request = "INSERT INTO Products (name, store, cat_id, grade, product_url) VALUES (%s, %s, %s, %s, %s)"
        val = (self.name, 
            self.store, self.cat_id, 
            self.grade, self.url)
        mycursor.execute(request, val)


class Category(object):
    '''One category contain bar code of all its products into a list'''

    def __init__(self, cat_name):
        self.name = cat_name
        self.cat_url = cat_url + cat_name + "/"

    def create_product_list(self, cat_id, mycursor):
        '''we append the list'''

        nb_page = 1
        nb_prod = 0
        while nb_prod < 50:
            category = requests.get(self.cat_url + str(nb_page) + '.json').json()
            p_name = ""
            p_grade = ""
            p_store = ""
            p_url = ""
            p_catid = cat_id
            product = Product()
            for p in category["products"]:
                try:
                    p_name = p["product_name"]
                    p_grade = p["nutrition_grade_fr"]
                    p_store = p["stores"]
                    p_url = p["url"]
                except KeyError:
                    pass

                if nb_prod < 50:
                    product.create_prod(p_name, p_grade, p_store, p_url, p_catid, mycursor)
                    nb_prod += 1
                else:
                    break

        nb_page += 1


    def insert_into_db(self, mycursor):
        '''we insert datas into DB'''

        request = "INSERT INTO Categories (name) VALUES (%s)"
        val = (self.name,)
        mycursor.execute(request, val)


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
