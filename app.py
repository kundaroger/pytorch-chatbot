from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_ngrok import run_with_ngrok

from chat import get_response, langdetect, translate 

app = Flask(__name__)
CORS(app)
run_with_ngrok(app)

@app.route("/",methods=['get'])
def index_get():
  return render_template("base.html")

@app.route("/predict",methods=['post'])
def predict():
  text = request.get_json().get("message")
  response = get_response(text)
  message = {"answer": response}
  return jsonify(message)
  

if __name__ == "__main__":
  app.run()