import requests
import mysql.connector
from constants import api_url, product_url, cat_url
from IDs import username, pw


class Product(object):

    def __init__(self, barcode, cat):
        self.code = barcode
        self.api_url = api_url + barcode +'.json'
        self.url = product_url + barcode
        self.category = cat
        self.product = {"code": "", "name": "", "store": "", "grade": "", "product_url": "", "category": ""}

    def create_prod(self):
        request = requests.get(self.api_url).json()
        if 'nutrition_grade_fr' in request['product'] and 'stores' in request['product']:
            self.product['code'] = self.code
            self.product['name'] = request['product']['product_name']
            self.product['store'] = request['product']['stores']
            self.product['grade'] = request['product']['nutrition_grade_fr']
            self.product['product_url'] = self.url
            self.product['category'] = self.category
        else:
            self.product = 0

    def save_prod(self, mycursor, mydb):
        if self.product != 0:
            request = "INSERT INTO Products (code, name, store, grade, product_url) VALUES (%s, %s, %s, %s, %s)"
            val = (self.product["code"], self.product["name"], self.product["store"], self.product["grade"], self.product["product_url"])
            mycursor.execute(request, val)
            mydb.commit()


class Category(object):

    def __init__(self, cat_name):
        self.name = cat_name
        self.cat_url = cat_url + cat_name + "/"
        self.product_list = []

    def create_product_list(self):
        i = 1
        while i != 0:
            cat = requests.get(self.cat_url + str(i) + '.json').json()
            if len(cat["products"]) != 0:
                for j in range(0, len(cat["products"])):
                    code = cat['products'][j]['code']
                    request = requests.get(api_url + code + '.json').json()
                    if 'nutrition_grade_fr' in request['product'] and 'stores' in request['product']:
                        if len(self.product_list) < 50:
                            self.product_list.append(code)
                        else:
                            i = -1
                            break
            else:
                break
            i += 1

    def insert_into_db(self, mycursor, mydb):
        request = "INSERT INTO Categories (name) VALUES (%s)"
        val = (self.name,)
        mycursor.execute(request, val)
        mydb.commit()


