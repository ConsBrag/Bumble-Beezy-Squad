import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

template_dir = os.path.abspath('./GeneratorApp')
app = Flask(__name__, template_folder=template_dir)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')