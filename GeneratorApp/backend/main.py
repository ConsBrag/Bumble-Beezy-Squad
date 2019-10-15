import os
import parser
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS

template_dir = os.path.abspath('..')
app = Flask(__name__, template_folder=template_dir)
CORS(app)

app.config['DOCX_USER'] = 'D:/!Git/Bumble-Beezy-Squad/GeneratorApp/backend/MSword'

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    print(request.json['name'])
    #parser.getTextOnTopic(request.json['Topics'], int(request.json['CountWord']))
    return jsonify(message ='True')
  #parser.getTextOnTopic(['physics', 'law'])
  return render_template('index.html')

@app.route('/diplom')
def download():
  return send_from_directory(app.config['DOCX_USER'], filename = "template.docx", as_attachment=False)