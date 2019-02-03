from app import app
import re
import pandas as pd
from app.services import *
from flask import request

@app.route('/')
def index():
    return 'Hello Cinnecta'

@app.route('/vocabulario',methods =['POST'])
def vocabulario():
    wordlist=getherTexts(request.json)
    vocabulario=filterUnique(wordlist)
    result ='\n'.join(vocabulario)
    return result



@app.route('/wordcount',methods =['POST'])
def wordcount():
    wordlist=getherTexts(request.json)
    vocabulario=filterUnique(wordlist)
    result=[]
    for content in request.json:
        words = split_text(content['text'])
        wordCount=countWords(vocabulario,words)
        result.append ( content['textname']+ ':'+ wordCount)
    result= '\n'.join(result)
    return result

@app.route('/fullwordcount',methods =['POST'])
def fullwordcount():
    wordlist=getherTexts(request.json)
    vocabulario=filterUnique(wordlist)
    wordCount=countWords(vocabulario,wordlist)
    result= str(wordCount)
    return result

def count_occurrences(word, sentence):
    return sentence.lower().split().count(word)

