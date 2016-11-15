
# coding: utf-8

# ## T3. Twitter에서 'Seoul' 10개 검색하기

# In[1]:

import os
keyPath=os.path.join(os.getcwd(),'src','twitter.properties')
print keyPath

f=open(keyPath,'r')
lines=f.readlines()

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    lines=f.readlines()
    for line in lines:
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d

key=getKey(keyPath)


# In[2]:

import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])


# In[3]:

client = oauth.Client(consumer, token)


# In[4]:

help(client.request)


# In[5]:

import urllib
url1 = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul','count':20}
mybody=urllib.urlencode(myparam)

resp, tsearch = client.request(url1+"?"+mybody, method="GET")
tsearch_json = json.loads(tsearch)


# In[6]:

print type(tsearch_json)
print tsearch_json.keys()
print len(tsearch_json['statuses'])


# In[7]:

len(tsearch_json['statuses'][0])


# In[8]:

for i,tweet in enumerate(tsearch_json['statuses']):
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])

