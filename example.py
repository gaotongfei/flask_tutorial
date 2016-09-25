# example.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/user/<name>')
def user(name):
    return 'hello ' + name

@app.route('/page/<int:page_id>')
@app.route('/page/<page_id>')
def page(page_id):
    if isinstance(page_id, str):
        return 'page id cannot be string type'
    elif isinstance(page_id, int):
        return 'page ' + str(page_id)

if __name__ == '__main__':
    app.run(debug=True)
