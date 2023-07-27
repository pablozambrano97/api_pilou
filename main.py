from flask import Flask, jsonify, request
import contacts_controller
from db import create_tables

app = Flask(__name__)


@app.route('/contacts', methods=[" GET"])
def get_contacts():
    contacts = contacts_controller.get_contacts()
    return jsonify(contacts)

@app.route("/contacts", methods=["POST"])
def insert_contact():
    contact_details=request.get_json()
    name = contact_details["name"]
    age = contact_details["age"]
    phone = contact_details["phone"]
    photo = contact_details["photo"]
    email = contact_details["email"]
    nick = contact_details["nick"]
    result = contacts_controller.insert_contact(name, age, phone, photo, email, nick)
    return jsonify(result)

@app.route("/contacts", methods=["PUT"])
def update_contact():
    contact_details=request.get_json()
    name=contact_details["name"]
    age=contact_details["age"]
    phone=contact_details["phone"]
    photo=contact_details["photo"]
    email=contact_details["email"]
    nick=contact_details["nick"]
    result = contacts_controller.update_contact(name, age, phone, photo, email, nick, email)
    return jsonify(result)

@app.route("/contacts/<email>", methods=["DELETE"])
def delete_contact(email):
    result=contacts_controller.delete_contact(email)
    return jsonify(result)

@app.route("/contacts/<age>", methods=["GET"])
def consult_contact_age(age):
    result=contacts_controller.consult_contact_age(age)
    return jsonify(result)

@app.route("/contacts/<email>", methods=["GET"])
def consult_contact_email(email):
    result=contacts_controller.consult_contact_email(email)
    return jsonify(result)

@app.route("/contacts/<phone>", methods=["GET"])
def consult_contact_phone(phone):
    result=contacts_controller.consult_contact_phone(phone)
    return jsonify(result)

"""
Enable CORS. Disable it if you don't need CORS
"""

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"]= "*"
    response.headers["Access-Control-Allow-Credentials"]= "true"
    response.headers["Access-Control-Allow-Methods"]= "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"]= "Accept, Content-Type, Content-Length, Accept Encoding, X-CSRF-Token"
    return response

if __name__ == '__main__':
    from waitress import serve
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=False)