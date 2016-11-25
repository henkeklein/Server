from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('startpage.html')

def add_person(form):
    f = open("forms.json")
    data = json.load(f)
    data["forms"].append(form)
    f.close()

    writing_file = open('forms.json', 'w')
    writing_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',',': ')))
    writing_file.close()

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
    add_person(data_dict)
    return render_template('done.html', title=title, author=author)
@app.route('/forms', methods=['GET'])
def get_forms():
  with open('forms.json', 'r') as f:
     return render_template('listforms.html', forms=json.loads(f.read())['forms'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/forms/<title>', methods=['GET'])
def get_one_form(title):
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
if __name__ == "__main__":
    app.run()
