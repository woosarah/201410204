
# coding: utf-8

# In[1]:

import os
keyPath=os.path.join(os.getcwd(),'twitter.properties')
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
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'FantasticBeasts','count':200,'since_id':'781131936664137728'}
mybody=urllib.urlencode(myparam)
response, content = client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)


# In[6]:

tsearch_json['statuses'][-1]['id']-1


# In[7]:

tsearch_json


# In[8]:

len(tsearch_json['statuses'])


# In[9]:

for tweet in tsearch_json['statuses']:
    print tweet['id']


# In[10]:

for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id']


# In[11]:

f=open('twitter_1.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id'],tweet['text']
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
f.close()


# In[12]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'FantasticBeasts','count':200,'since_id':'808024153148137473'}
mybody=urllib.urlencode(myparam)
response, content = client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)
tsearch_json['statuses'][-1]['id']-1


# In[13]:

for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id']


# In[14]:

f=open('twitter_2.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id'],tweet['text']
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
f.close()


# In[15]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'FantasticBeasts','count':200,'since_id':'808030255348731904'}
mybody=urllib.urlencode(myparam)
response, content = client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)
tsearch_json['statuses'][-1]['id']-1


# In[16]:

for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id']


# In[17]:

f=open('twitter_3.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id'],tweet['text']
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
f.close()


# In[18]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'FantasticBeasts','count':200,'since_id':'808032027148746754'}
mybody=urllib.urlencode(myparam)
response, content = client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)
tsearch_json['statuses'][-1]['id']-1


# In[19]:

for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id']


# In[20]:

f=open('twitter_4.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id'],tweet['text']
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
f.close()


# In[21]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'FantasticBeasts','count':200,'since_id':'808032786280022016'}
mybody=urllib.urlencode(myparam)
response, content = client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)
tsearch_json['statuses'][-1]['id']-1


# In[22]:

for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id']


# In[23]:

f=open('twitter_5.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id'],tweet['text']
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
f.close()


# In[1]:

import findspark
import os
spark_home="C:\Users\LG\Downloads\spark-1.6.0-bin-hadoop2.6"
findspark.init(spark_home)


# In[2]:

import pyspark
conf=pyspark.SparkConf()
conf = pyspark.SparkConf().setAppName("myAppName")
sc = pyspark.SparkContext(conf=conf)


# In[3]:

textFile=sc.textFile("src/twitter_1.txt")
type(textFile)


# In[4]:

_sparkLIne=textFile.filter(lambda line:"Newt" in line)
_sparkLIne.count()


# In[6]:

_sparkLIne=textFile.filter(lambda line:"Credence" in line)
_sparkLIne.count()


# In[7]:

_sparkLIne=textFile.filter(lambda line:"Graves" in line)
_sparkLIne.count()


# In[8]:

textFile=sc.textFile("src/twitter_2.txt")
type(textFile)


# In[9]:

_sparkLIne=textFile.filter(lambda line:"Newt" in line)
_sparkLIne.count()


# In[10]:

_sparkLIne=textFile.filter(lambda line:"Credence" in line)
_sparkLIne.count()


# In[11]:

_sparkLIne=textFile.filter(lambda line:"Graves" in line)
_sparkLIne.count()


# In[12]:

textFile=sc.textFile("src/twitter_3.txt")
type(textFile)


# In[13]:

_sparkLIne=textFile.filter(lambda line:"Newt" in line)
_sparkLIne.count()


# In[14]:

_sparkLIne=textFile.filter(lambda line:"Credence" in line)
_sparkLIne.count()


# In[15]:

_sparkLIne=textFile.filter(lambda line:"Graves" in line)
_sparkLIne.count()


# In[26]:

textFile=sc.textFile("src/twitter_4.txt")
type(textFile)


# In[27]:

_sparkLIne=textFile.filter(lambda line:"Newt" in line)
_sparkLIne.count()


# In[28]:

_sparkLIne=textFile.filter(lambda line:"Credence" in line)
_sparkLIne.count()


# In[29]:

_sparkLIne=textFile.filter(lambda line:"Graves" in line)
_sparkLIne.count()


# In[30]:

textFile=sc.textFile("src/twitter_5.txt")
type(textFile)


# In[31]:

_sparkLIne=textFile.filter(lambda line:"Newt" in line)
_sparkLIne.count()


# In[32]:

_sparkLIne=textFile.filter(lambda line:"Credence" in line)
_sparkLIne.count()


# In[33]:

_sparkLIne=textFile.filter(lambda line:"Graves" in line)
_sparkLIne.count()


# In[34]:

_sparkLIne=textFile.filter(lambda line:"Pickett" in line)
_sparkLIne.count()


# Newt= 4
# Credence=3
# Graves=2
