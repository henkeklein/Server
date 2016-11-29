from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('startpage.html')

#--------------------ADD NEW FORM---------------

def add_form(form):
    f = open("forms.json")
    data = json.load(f)
    data["forms"].append(form)
    f.close()

    writing_file = open('forms.json', 'w')
    writing_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',',': ')))
    writing_file.close()

#--------------------DONE METHOD WHEN ADDED NEW---------------

@app.route('/done', methods=['POST'])
def form_post():
    title = request.form['title']
    author = request.form['author']
    content = request.form['content']

    data_dict = {
        "title":title,
        "author":author,
        "content":content
    }
    add_form(data_dict)
    return render_template('done.html', title=title, author=author)

#--------------------GET ALL FORMS---------------

@app.route('/forms', methods=['GET'])
def get_forms():
  with open('forms.json', 'r') as f:
     return render_template('listforms.html', forms=json.loads(f.read())['forms'])

@app.route('/api/forms', methods=['GET'])
def get_json():
  with open('forms.json', 'r') as f:
      forms = json.load(f)
      return jsonify(forms)

#--------------------ERROR---------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#--------------------GET ONE FORM BY TITLE---------------

@app.route('/api/forms/<title>', methods=['GET'])
def profile(title):
      with open('forms.json', 'r') as f:
        forms = json.load(f)
        for key, value in forms.items():
            for form in value:
                if(form['title']== title):
                    data_dict = {
                        "title":form['title'],
                        "author":form['author'],
                        "content":form['content'],
                        }
                    return jsonify(data_dict)

@app.route('/forms/<title>/', methods=['GET'])
def get_one_form(title):
      with open('forms.json', 'r') as f:
        forms = json.load(f)
        for key, value in forms.items():
            for form in value:
                if(form['title']== title):
                    title = form['title']
                    author = form['author']
                    content = form['content']
                    return render_template('listone.html', title=title, author=author, content=content)

#--------------------EDIT ONE FORM---------------

@app.route('/forms/<title>/edit', methods=['GET'])
def edit_one_form(title):
    with open('forms.json', 'r') as f:
        forms = json.load(f)
        for key, value in forms.items():
            for form in value:
                if(form['title']== title):
                    title = form['title']
                    author = form['author']
                    content = form['content']
                    data_dict = {
                        "title":title,
                        "author":author,
                        "content":content
                        }
                    return render_template('editForm.html', title=title, author=author, content=content)

@app.route('/forms/<title>/edit/done', methods=['POST'])
def save_edit_form(title):
    data = json.load(open('forms.json'))
    for key, value in data.items():
        for form in value:
            if(form['title']== title):
                data_dict = {
                "title": request.form['title'],
                "author": request.form['author'],
                "content": request.form['content'],
                }
                data["forms"].append(data_dict)

                for i in xrange(len(data["forms"])):
                    if data["forms"][i]["title"] == title:
                        data["forms"].pop(i)
                        break

    writing_file = open('forms.json', 'w')
    writing_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    writing_file.close()
    return render_template('updatedForm.html')

if __name__ == "__main__":
    app.run()
