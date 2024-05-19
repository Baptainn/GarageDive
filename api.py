from flask import Flask, request, render_template, jsonify
import database_api

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def route1():
   return render_template('list.html')

@app.route('/signup')
def route2():
   return render_template('signup.html')

@app.route('/login-screen')
def route3():
   return render_template('login.html')

@app.route('/add-screen')
def route4():
   return render_template('additem.html')

@app.route('/main')
def route5():
   return render_template('normal.html')

@app.route('/create-account', methods=['POST'])
def create_account():
   data = request.json

   first = data['first']
   last = data['last']
   email = data['email']
   password = data['pass']
   location = data['location']

   return_string = ""
   try:
      database_api.create_account(first, last, email, password, location, None)
   except Exception as exception:
      return_string = str(exception)
      print(exception)

   result = {
      "output": return_string
   }
   
   result = {str(key): value for key, value in result.items()}
   return jsonify(result=result)

@app.route('/create-item', methods=['POST'])
def create_item():
   data = request.json

   name = data['name']
   price = data['price']
   email = data['email']
   password = data['pass']

   return_string = ""
   try:
      database_api.upload_item(email, password, name, price, "")
   except Exception as exception:
      return_string = str(exception)
      print(exception)

   result = {
      "output": return_string
   }
   
   result = {str(key): value for key, value in result.items()}
   return jsonify(result=result)

@app.route('/login', methods=['POST'])
def login():
   data = request.json

   email = data['email']
   password = data['pass']

   return_string = ""
   try:
      database_api.validate_account(email, password)
   except Exception as exception:
      return_string = str(exception)
      print(exception)

   result = {
      "output": return_string
   }
   
   result = {str(key): value for key, value in result.items()}
   return jsonify(result=result)

@app.route('/list-search', methods=['POST'])
def list_search():
   result = {}
   try:
      result = database_api.get_item_list("")
   except Exception as exception:
      return_string = str(exception)
      print(exception)
   
   result = {str(key): value for key, value in result.items()}
   return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

