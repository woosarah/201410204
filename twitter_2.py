
# coding: utf-8

# ## T2_ 자신의 타임라인 가져오기

# In[1]:

import os
keyPath=os.path.join(os.getcwd(),'src','twitter.properties')
print keyPath


# In[2]:

f=open(keyPath,'r')
lines=f.readlines()


# In[3]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    lines=f.readlines()
    for line in lines:
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[4]:

key=getKey(keyPath)


# In[6]:

import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])


# In[7]:

client = oauth.Client(consumer, token)


# In[8]:

from pymongo import MongoClient


# In[9]:

_mclient=MongoClient()


# In[10]:

_mclient['ds_twitter']


# In[11]:

_db=_mclient.ds_twitter


# In[12]:

_col=_db.home_timeline


# In[19]:

url="https://api.twitter.com/1.1/statuses/home_timeline.json"


# In[20]:

response, content=client.request(url)


# In[21]:

home_timeline=json.loads(content)


# In[22]:

len(home_timeline)


# In[23]:

print home_timeline


# In[24]:

for tweet in home_timeline:
    print tweet ['id'],tweet['text']
    _col.insert_one(tweet)

