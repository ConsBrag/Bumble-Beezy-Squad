import json, requests
from bs4 import BeautifulSoup

# topics - МАССИВ тем по диплому (не кидать строку, даже если элемент один)
def getTextOnTopic(topics):
  topic = '+'.join(topics)
  response = requests.get('http://yandex.ru/referats/?t='+topic)
  text = parseText(response.text)
  print(text)

# def getText

def parseText(html):
  soup = BeautifulSoup(html, 'lxml')
  paragraphs = []
  text = soup.find('div', class_='referats__text')
  topic = text.find('strong').text
  paragraph = text.find_all('p')
  for i in paragraph:
    paragraphs.append(i.text)
  
  print(paragraphs)
  return json.dumps({'topic': topic, 'paragraphs': paragraphs})