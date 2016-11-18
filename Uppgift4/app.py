from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def main():
    #return 'This is the homepage'
    return render_template('presentation.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/movies')
def movies():
    movie_list = ['Tropic Tunder', 'Star Wars', 'The Dark Knight', 'Pulp Fiction', 'Inception']
    return render_template('movies.html', lst=movie_list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/hello/<username>')
def profile(username):
    return "<h2>Hello %s<h2>" %username
    if __name__ == "__main__":
        app.run()
