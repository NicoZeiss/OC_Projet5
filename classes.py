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
        r = requests.get(self.api_url).json()
        self.product['code'] = self.code
        self.product['name'] = r['product']['product_name']
        self.product['store'] = r['product']['stores']
        self.product['grade'] = r['product']['nutrition_grade_fr']
        self.product['product_url'] = self.url
        self.product['category'] = self.category

    # def save_prod(self):


class Category(object):

    def __init__(self, cat_name):
        self.name = cat_name
        self.cat_url = cat_url + cat_name + '.json'
        self.product_list = []

    def create_product_list(self):
        cat = requests.get(self.cat_url).json()
        for i in range(0, cat['page_size']):
            code = cat["products"][i]["code"]
            self.product_list.append(code)

    # def insert_into_db(self):




        


