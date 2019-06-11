import requests
import mysql.connector
from constants import api_url, product_url
from IDs import username, pw


class Product(object):

    def __init__(self, barcode, cat):
        self.code = barcode
        self.api_url = api_url + barcode +'.json'
        self.url = product_url + barcode
        self.category = cat

    def create_prod(self):
        r = requests.get(self.api_url).json()
        product = {"code": "", "name": "", "store": "", "grade": "", "product_url": "", "category": ""}
        product['code'] = self.code
        product['name'] = r['product']['product_name']
        product['store'] = r['product']['stores']
        product['grade'] = r['product']['nutrition_grade_fr']
        product['product_url'] = self.url
        product['category'] = self.category

    def save_prod(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = username,
            passwd = pw,
            database = "projet5")
        mycursor = mydb.cursor()
        sql = "INSERT INTO Products"


        


