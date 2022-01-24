import json
import os
import macpath
from textblob import TextBlob
import marshal
import subprocess
import math
import secrets


def parse(path):
  g = open(path, 'r')
  for l in g:
    yield eval(l)
a=0
currentId=None
sum=0
rCount=0
for review in parse('./reviews_Amazon_Instant_Video_5.json'):
    if a<20:
        if(currentId is None):
            currentId = review['asin']
    
        if(currentId != review['asin']):
            print('\n\n\n\n Average Polarity: '+str((sum/rCount)))
            rCount=0
            sum=0
            currentId=review['asin']
        
        rCount=rCount+1
        analysis = TextBlob(review['reviewText'])
        print(review['asin'])
        print(' ' +' '+ str(analysis.sentiment)+ '\n\n')
        sum=sum+analysis.sentiment.polarity
    
