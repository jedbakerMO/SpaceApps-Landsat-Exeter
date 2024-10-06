from flask import Flask, request, render_template
from app import app

@app.route("/", methods=['GET'])
def input_field():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def input_field_post():
    text = request.form['text'] # TODO: Change 'text' to whatever it's called
    api_response = some_request(text) # TODO: send request to API
    # TODO: Change function ^^^
    return api_response


