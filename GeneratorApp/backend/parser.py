import json, requests, time, pymorphy2, os, glob
from bs4 import BeautifulSoup
from entity.diplom import Diplom
from time import sleep
import urllib.request

images_dir = os.path.abspath('../images/')

wordsCount = 0
firstIteration = 0

# topics - МАССИВ тем по диплому (не кидать строку, даже если элемент один)
def getTextOnTopic(topics, countWords):  
  global wordsCount
  global firstIteration
  firstIteration = 0
  wordsCount = 0
  diplom = Diplom()
  
  removeImages()

  topic = '+'.join(topics)
  while wordsCount < countWords:
    response = requests.get('http://yandex.ru/referats/?t='+topic)
    parseText(response.text, diplom)
  
  return diplom

def removeImages():
  filelist = glob.glob(os.path.join(images_dir, "*.jpg"))
  for f in filelist:
    os.remove(f)

def parseText(html, diplom):
  global firstIteration
  global wordsCount

  soup = BeautifulSoup(html, 'lxml')
  text = soup.find('div', class_='referats__text')
  if not firstIteration:
    diplom.topic = text.find('strong').text
    firstIteration = 1
  
  paragraph = text.find_all('p')
  for i in paragraph:
    diplom.paragraphs.append(i.text)
    getImage(i.text)
    wordsCount += len(i.text.split())

def getImage(txt):
  noun = getNoun(txt)
  response = requests.post('https://ru.depositphotos.com/stock-photos/'+noun+'.html?filter=all')
  soup = BeautifulSoup(response.text, 'lxml')
  text = soup.find('img', class_='file-container__image')['src']
  urllib.request.urlretrieve(text, images_dir+'/'+noun+'.jpg')

def getNoun(txt):
  morph = pymorphy2.MorphAnalyzer()
  newdata = ''
  nouns_with_counts = {}
  for i in txt:
    if i.lower() not in ' -абвгдеёжзийклмнопрстуфхцчшщъыьэюя' or i == '\n' or i == '\v' or i == '\t':
      txt = txt.replace(i, '').lower()
  
  newdata += txt + ' '
  newdata = newdata.split()
  
  for word in newdata:
    p = morph.parse(word)[0]
    if p.tag.POS == 'NOUN' and p.score > 0.5:
      nouns_with_counts[p.normal_form] = nouns_with_counts.get(p.normal_form, 0) + 1
  
  nouns_with_counts = [x[0] for x in
    sorted(nouns_with_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)]
  
  return nouns_with_counts[0] + '-' + nouns_with_counts[1]
  