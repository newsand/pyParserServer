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

