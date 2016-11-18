from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('startpage.html')

def add_person(person):
    f = open("people.json")
    data = json.load(f)
    data["people"].append(person)
    f.close()

    writing_file = open('people.json', 'w')
    writing_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',',': ')))
    writing_file.close()

@app.route('/done', methods=['POST'])
def form_post():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    secNumber = request.form['secNumber']
    email = request.form['email']
    address = request.form['address']
    comments = request.form['comments']

    data_dict = {
        "firstname":firstname,
        "lastname":lastname,
        "secNumber":secNumber,
        "email":email,
        "address":address,
        "comment":comments
    }
    add_person(data_dict)
    return render_template('done.html', firstname=firstname, lastname=lastname, secNumber=secNumber, email=email, address=address, comments=comments)
@app.route('/users', methods=['GET'])
def get_persons():
  with open('people.json', 'r') as f:
    return render_template('listpersons.html', people=json.loads(f.read())['people'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/users/:ssn')
def profile(username):
    return "<h2>Hello %s<h2>" %username
    if __name__ == "__main__":
        app.run()
