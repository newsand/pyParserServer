# pyParserServer

running with py3

uses: 
flask
falsk-alchemy
flask-restless
sqlite  
flask-requests

accept json to post on body with raw JSON(application/json) 
with format like 

[
  {
    "text": "É fácil escrever código. Difícil é escrever código que funcione.",
    "textname": "texto2.txt"
  },
  {
    "text": "Falar é fácil. Mostre-me o código.",
    "textname": "texto1.txt"
  }
]

Running project

go to dir: \pyParserServer\API\APIRest
use the command 
python run.py