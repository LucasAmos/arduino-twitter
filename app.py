from flask import Flask
import tweeter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/tweet/<string:username>', methods=['GET'])
def reading_latest(username):

    reading = tweeter.user_tweet(username)

    return json.dumps(reading)