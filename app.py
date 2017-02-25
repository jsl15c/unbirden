from flask import flask


app = Flask(__name__)

# routing/mapping to tie url to python
# function
@app.route('/')
def index();
    return 'This is the homepage'
