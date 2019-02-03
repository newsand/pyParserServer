from app import app
from app import db
from app import manager
from app.models import texts
import re
import pandas as pd

def split_text(_text):
    _text.lower()
    words = re.split(' |\.',_text)
    words = list(filter(None, words))
    return words

def filterUnique(_wordList):
    unique = set(_wordList)
    return unique

def countWords(_uniqueSet,_fullSet):
    for word in _uniqueSet:
        print (word,' : ',_fullSet.count(word))
    return 'ok'


def split_2gram(_text):
    # primalWords = split_text(_text)
    # words2gram
    return 'ok'


def getx():
    return  Texts.query.first()