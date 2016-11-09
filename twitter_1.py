
# coding: utf-8

# ## T1. Twitter에 ''를 쓴다.

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


# In[5]:

import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])


# In[6]:

client = oauth.Client(consumer, token)


# In[7]:

help(client.request)


# In[8]:

import urllib
url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': '이제 난 파이썬으로 트위터에 별 소리를 다 쓸 수 있다'})
response,content=client.request(url,method='POST',body=mybody)


# In[9]:

import io
with io.open('src/ds_twitter_1.json', 'w', encoding='utf8') as json_file:
    data=json.dumps(content, json_file, ensure_ascii=False, encoding='utf8')
    json_file.write(data)

