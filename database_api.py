import json
import re
from uuid import uuid4 as new_guid

class Item:
    def __init__(self, name, id_, author, location, price, image):
        self.name = name
        self.id = id_
        self.author = author
        self.location = location
        self.price = price
        self.image = image or ""

class Author:
    def __init__(self, first, last, email, password, location, image):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.password = password
        self.location = location
        self.image = image or ""

def validate_account(email, password):
    with open('database.json') as database:
        data = json.load(database)

    if not email in data['authors'].keys():
        raise Exception("The email or password that you entered is incorrect.")

    author = data['authors'][email]
    if not author['password'] == password:
        raise Exception("The email or password that you entered is incorrect.")

    return True

def upload_item(email, password, item_name, item_price, item_image):
    item_image = item_image or ""
    item_price = float(item_price)
    item_id = str(new_guid())

    validate_account(email, password)
    
    print(f"New item created with the id: {item_id}!")

    with open('database.json') as database:
        data = json.load(database)

    location = data['authors'][email]['location']
    
    entry = {item_id:
        {
            "item_name": item_name,
            "item_author": email,
            "item_location": location,
            "price": item_price,
            "image": item_image
        }
    }
    data['items'].update(entry)

    with open('database.json', 'w') as database:
        json.dump(data, database, indent=4)

def get_item_list(user):
    with open('database.json') as database:
        data = json.load(database)

    if user == "":
        return data['items']

email_match = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def create_account(first, last, email, password, location, image):
    image = image or ""

    if not re.fullmatch(email_match, email):  
        raise Exception("Invalid email!")
    
    with open('database.json') as database:
        data = json.load(database)

    if email in data['authors'].keys():
        raise Exception("Account already exists.")

    print(f"New account created with the email: {email}!")
    
    entry = {email:
        {
            "first_name": first,
            "last_name": last,
            "password": password,
            "location": location,
            "image": image
        }
    }
    data['authors'].update(entry)

    with open('database.json', 'w') as database:
        json.dump(data, database, indent=4)

def delete_item(item_id):
    with open('database.json') as database:
        data = json.load(database)

    if not item_id in data['items'].keys():
        raise Exception("Key does not exist!")

    del data['items'][item_id]

    print(f"Item deleted with the id: {item_id}!")
    
    with open('database.json', 'w') as database:
        json.dump(data, database, indent=4)

#delete_item("3a85e295-ad64-47a0-a1bb-c1200e0e67be")
#upload_item(Author("John", "Smith", "j@s.com", "123", "quebec", ""), "test", 29.99, "test")
