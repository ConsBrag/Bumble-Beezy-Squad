import json, requests, time
from bs4 import BeautifulSoup
from entity.diplom import Diplom

wordsCount = 0
firstIteration = 0

# topics - МАССИВ тем по диплому (не кидать строку, даже если элемент один)
def getTextOnTopic(topics, countWords):
  global wordsCount
  global firstIteration
  firstIteration = 0
  wordsCount = 0
  diplom = Diplom()

  topic = '+'.join(topics)
  while wordsCount < countWords:
    response = requests.get('http://yandex.ru/referats/?t='+topic)
    parseText(response.text, diplom)
  
  return diplom

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
    wordsCount += len(i.text.split())