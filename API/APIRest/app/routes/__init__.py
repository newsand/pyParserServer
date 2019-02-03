from app import app
import re
import pandas as pd
from app.services import *

@app.route('/')
def index():
    x = getx()
    print(x)
    return 'Hello Cinnecta'


@app.route('/vocabulario')
def vocabulario():
    return 'RELOUtester'


@app.route('/vocabulario2gram')
def vocabulario2Gram():
    return 'RELOUtester'


@app.route('/wordcount')
def wordcount():
    return 'RELOUtester'

@app.route('/wordcount2gram')
def wordcount2gram():
    return 'RELOUtester'



@app.route('/parse')
def parsse():
    texto = 'É fácil escrever código. Difícil é escrever código que funcione.'
    words =split_line(texto)
    str1 = ''.join(str(e) for e in words)
    return str1


@app.route('/wordCount')
def wordCount():
    _text = 'É fácil escrever código. Difícil é escrever código que funcione.'
    _text= _text.lower()
    dictio=split_text(_text)
    d = {'words': [], 'counts': []}
    for word in dictio:
        print(word)
        counts = count_occurrences(word, _text)
        d['words'].append(word)
        d['counts'].append(counts)
    print(d)
    return 'ok'

def split_line(_text):
    #split the text
    words = re.split(' |\.',_text)
    words = list(filter(None, words))
    print (words)
    s = pd.Series(words)
    print('woot')
    print(s.value_counts())
    
    unique = set(words)
    print(unique)

    # for each word in the line:
    # for word in words:
    #     # print the word
    #     print(word)
    return unique

def count_occurrences(word, sentence):
    return sentence.lower().split().count(word)

