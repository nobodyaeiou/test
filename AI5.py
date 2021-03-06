# -*- coding: utf-8 -*-
"""AI5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14VsZfwaY7FPWwXij7RwCfoOBFC5Mtvvk
"""

import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

pip install nltk

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only

f = open("/content/drive/MyDrive/Ai/chatbot.txt","r" ,errors = 'ignore')
raw=f.read()
raw = raw.lower() # converts to lowercase

from google.colab import drive
drive.mount('/content/drive')

sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    Atharvabot_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        Atharvabot_response=Atharvabot_response+"I am sorry! I don't understand you"
        return Atharvabot_response
    else:
        Atharvabot_response = Atharvabot_response+sent_tokens[idx]
        return Atharvabot_response

flag=True
print("Atharvabot: My name is Atharvabot. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Atharvabot: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("Atharvabot: "+greeting(user_response))
            else:
                print("Atharvabot: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Atharvabot: Bye! take care..")