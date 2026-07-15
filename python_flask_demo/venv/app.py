from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    print("Flask is roaming")
    return 'hello'