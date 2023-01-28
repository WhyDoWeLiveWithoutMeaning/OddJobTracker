from quart import Quart, jsonify, render_template, redirect, request

from Communication import Database
from Objects import UserAlreadyExists

app = Quart(__name__)

db = Database('test.db')

@app.route('/')
async def index():
    return await render_template(
        'index.html',
        people=db.get_people()
    )

@app.route('/add/person')
async def hola():
    first_name = request.args.get('fname')
    last_name = request.args.get('lname')
    try:
        db.add_person(first_name, last_name)
        return redirect('/')
        return jsonify({'message': 'Added ' + first_name + ' ' + last_name})
    except UserAlreadyExists:
        return jsonify({"error" : "this user already exists"}), 409

@app.route('/get/person/<first_name>/<last_name>')
async def get(first_name, last_name):
    return jsonify(db.get_person(first_name, last_name).to_dict())

if __name__ == '__main__':
    db.create_table()
    app.run(port=5500, debug=True)