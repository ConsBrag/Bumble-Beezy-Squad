import os
import parserS, docxgen
from entity.diplom import Diplom
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS

imagesPath = os.path.abspath('../images/')
template_dir = os.path.abspath('..')
app = Flask(__name__, template_folder=template_dir)
CORS(app)

app.config['DOCX_USER'] = 'D:/.Git/Bumble-Beezy-Squad/GeneratorApp/backend/MSword/'

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    namefile = ''
    if not os.path.isdir(imagesPath):
      os.makedirs(imagesPath)
    diplom = Diplom()
    diplom = parserS.getTextOnTopic(request.json['Topics'], int(request.json['CountWord']))
    namefile = docxgen.generateDocx(request.json['name'], request.json['lastName'], diplom)
    if namefile: return jsonify(message =namefile)
    return jsonify(message = 'False')

  return render_template('index.html')

@app.route('/<string:doc_name>')
def download(doc_name):
  print(app.config['DOCX_USER']+doc_name)
  return send_from_directory(app.config['DOCX_USER'], filename = doc_name, as_attachment=False)