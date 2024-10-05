from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/docs")
def docs():
    return render_template('docs.html')



if __name__ == "__main__":
  port = int(os.environ.get('PORT', 3030))
  app.run(debug=True, host='0.0.0.0', port=port)

