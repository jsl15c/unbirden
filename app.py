from flask import Flask, render_template, request
from twitter import getTweets

# import json
# from watson_developer_cloud import AlchemyLanguageV1
# alchemy_language = AlchemyLanguageV1(api_key='a04bf0cda38fd380a2e89b9b54d6076729b568ce')

app = Flask(__name__)


# routing/mapping to tie url to python
# function
@app.route('/')
def index():
    return render_template('input.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      handle = request.form['handle']
      tweets = getTweets(handle)
      return (tweet)
