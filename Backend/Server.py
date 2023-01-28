from quart import Quart, jsonify

from Communication import Database
from Objects import UserAlreadyExists

app = Quart(__name__)

db = Database('test.db')

@app.route('/')
async def index():
    return jsonify({'message': 'Hello World'})

@app.route('/add/person/<first_name>/<last_name>')
async def hola(first_name, last_name):
    try:
        db.add_person(first_name, last_name)
        return jsonify({'message': 'Added ' + first_name + ' ' + last_name})
    except UserAlreadyExists:
        return jsonify({"error" : "this user already exists"}), 409

@app.route('/get/person/<first_name>/<last_name>')
async def get(first_name, last_name):
    return jsonify(db.get_person(first_name, last_name).to_dict())

if __name__ == '__main__':
    db.create_table()
    app.run()