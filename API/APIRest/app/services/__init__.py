from app import app
from app import db
from app import manager
from app.models import texts
import re
import pandas as pd

def split_text(_text):
    fulltext=_text.lower()
    words = re.split('\s|(?<!\d)[,.-](?!\d)',fulltext)
    words = list(filter(None, words))
    return words

def filterUnique(_wordList):
    unique = set(_wordList)
    return unique

def countWords(_uniqueSet,_fullSet):
    result='['
    for word in _uniqueSet:
        result+=str(_fullSet.count(word))+',' 
    result = result[:-1]
    result+= ']'
    return result

def getherTexts(_textList):
    words=[]
    for content in _textList:
        words +=split_text(content['text'])
    return words

def getherTexts2Gram(_textList):
    words2Gram=[]
    for content in _textList:
        firstSplit=split_text(content['text'])
        words2Gram+=create2Grams(firstSplit)
    return words2Gram


def create2Grams(_wordList):
    lastword=_wordList[0]
    list2gram=[]
    wordlist=_wordList[1:]
    for word in wordlist:
        twoGram =lastword+' '+word
        lastword = word
        list2gram.append(twoGram)
    return list2gram
