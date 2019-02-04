# pyParserServer
Technologies
Python 3
flask
falsk-alchemy
flask-restless
sqlite  
flask-requests
Pandas

all apis below run as POST

APIs run on Localhost:8080

/vocabulario         -> return the list of words

/vocabulario2gram    -> return the list of words as a composite word

/wordcount           -> return the word count vector
\
/fullwordcount       -> return the wordcount as if the 2 texts are one

/wordcount2gram      -> return the word count vector with words as composite words

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
