import os
import parserS, docxgen
from entity.diplom import Diplom
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS

imagesPath = os.path.abspath('../images/')
template_dir = os.path.abspath('..')
app = Flask(__name__, template_folder=template_dir)
CORS(app)

app.config['DOCX_USER'] = 'D:/!Git/Bumble-Beezy-Squad/GeneratorApp/backend/MSword'

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    if not os.path.isdir(imagesPath):
      os.makedirs(imagesPath)
    print(request.json['name'])
    diplom = Diplom()
    diplom = parserS.getTextOnTopic(request.json['Topics'], int(request.json['CountWord']))
    docxgen.generateDocx(request.json['name'], request.json['lastname'], diplom)
    return jsonify(message ='True')
  #parser.getTextOnTopic(['physics', 'law'])
  return render_template('index.html')

@app.route('/diplom')
def download():
  return send_from_directory(app.config['DOCX_USER'], filename = "out.docx", as_attachment=False)