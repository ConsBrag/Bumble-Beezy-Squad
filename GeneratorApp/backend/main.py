import os
import parser
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

template_dir = os.path.abspath('../')
app = Flask(__name__, template_folder=template_dir)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def getDiplom():
  diplom = parser.getTextOnTopic(['physics', 'law'], 200) #Пример входных данных
  return 'True'