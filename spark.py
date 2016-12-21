
# coding: utf-8

# 라이브러리 설치
# pip install findspark

# In[1]:

import findspark


# C:\Users\LG-PC\Downloads\spark-1.6.0-bin-hadoop2.6

# In[2]:

import os
spark_home="C:\Users\LG\Downloads\spark-1.6.0-bin-hadoop2.6"


# In[3]:

print spark_home


# In[4]:

findspark.init(spark_home)


# In[5]:

import pyspark


# In[6]:

conf=pyspark.SparkConf()


# In[7]:

conf = pyspark.SparkConf().setAppName("myAppName")


# In[8]:

sc = pyspark.SparkContext(conf=conf)


# In[9]:

sc


# stand alone 방식

# In[10]:

sc.version


# In[11]:

sc.master


# In[12]:

sc._conf.getAll()


# ## S3. Hello RDD
# 스파크를 쓰려면 함수를 알아야함

# ## python 함수
# 함수는 헤더와 바디로 구분
# def 로 시작
# :로 마침
# 
# c2f : 화씨를 받아서 섭씨로 만드는 함수
# float : 형변환

# In[13]:

f=list([39.2, 36.5, 37.3, 37.0])
print f


# In[14]:

f[1]


# In[15]:

for x in f:
    print x,


# In[16]:

print 1./2


# In[17]:

print float(1)/2


# In[18]:

c=list([39.2, 36.5, 37.3, 37.0])
def c2f(c):
    f=list()
    for x in f:
        _c=9./5*x+32;
        f.append(_c)
    return f


# In[19]:

print c2f(c)


# ## map 함수

# In[20]:

map(lambda c:(float(9)/5)*c + 32, c)
##map 함수


# In[21]:

get_ipython().run_cell_magic(u'writefile', u'src/spark_wiki.txt', u"Wikipedia\nApache Spark is an open source cluster computing framework.\n\uc544\ud30c\uce58 \uc2a4\ud30c\ud06c\ub294 \uc624\ud508 \uc18c\uc2a4 \ud074\ub7ec\uc2a4\ud130 \ucef4\ud4e8\ud305 \ud504\ub808\uc784\uc6cc\ud06c\uc774\ub2e4.\nOriginally developed at the University of California, Berkeley's AMPLab,\nthe Spark codebase was later donated to the Apache Software Foundation,\nwhich has maintained it since.\nSpark provides an interface for programming entire clusters with\nimplicit data parallelism and fault-tolerance.")


# In[22]:

sc.textFile("src/spark_wiki.txt")


# In[23]:

textFile=sc.textFile("src/spark_wiki.txt")


# In[24]:

type(textFile)


# In[25]:

textFile.take(3)


# In[26]:

##토커나이제이션 tokenization
##' ' 는 공백
textFile.map(lambda x:x.split(' '))


# In[27]:

words=textFile.map(lambda x:x.split(' '))


# In[28]:

words.collect()


# In[29]:

##각 문장의 철자 갯수 세기
textFile.map(lambda x:len(x)).collect()


# ## Filter 함수

# In[30]:

_sparkLIne=textFile.filter(lambda line:"Spark" in line)


# In[31]:

_sparkLIne.count()
##이 중 3문장이 "Spark"라는 단어를 가지고 있다


# In[32]:

_sparkLIne=textFile.filter(lambda line:u"스파크" in line)


# In[33]:

_sparkLIne.count()
##걍 큰따옴표로 묶어서 한글치면 에러가 난다. 한글처리가 안됨...그래서 u"스파크"로 넣음


# In[34]:

print _sparkLIne.first()


# In[35]:

a=[1,2,3]


# In[36]:

type(a)


# In[37]:

myrdd=sc.parallelize(a)
##sc 없이는 아무것도 못한다네


# In[38]:

myrdd.take(3)


# In[39]:

squared=myrdd.map(lambda x:x*x)


# In[40]:

squared.collect()


# In[41]:

a=["this is a line","this is another line"]
myrdd=sc.parallelize(a)


# In[1]:

words=myrdd.map(lambda x:x.split(' '))


# In[43]:

words.collect()


# In[44]:

myrdd.map(lambda x:x.split('')).collect()


# In[45]:

myrdd.map(lambda x:x.replace("a","AA")).collect()


# In[46]:

get_ipython().run_cell_magic(u'writefile', u'src/spark_2cols.csv', u'35, 2\n40, 27\n12, 38\n15, 31\n21, 1\n14, 19\n46, 1\n10, 34\n28, 3\n48, 1\n16, 2\n30, 3\n32, 2\n48, 1\n31, 2\n22, 1\n12, 3\n39, 29\n19, 37\n25, 2')


# In[47]:

f=sc.textFile("src/spark_2cols.csv")


# In[48]:

csvRdd=f.map(lambda x:x.split(','))


# In[49]:

csvRdd.collect()


# ## dense vector

# In[50]:

from pyspark.mllib.linalg import Vectors
dv1=Vectors.dense([1, 2, 3])


# In[51]:

print dv1


# In[52]:

import numpy as np
dv2=np.array([1,2,3])


# In[53]:

Vectors.dense(dv2)


# In[54]:

sv1=Vectors.sparse(3,[1,2],[1.0,3.0])


# In[55]:

sv1.toArray()


# In[ ]:

from pyspark.mllib.regression import LabeledPoint
LabeledPoint(1.0,Vectors.dense(1.0,2.0,3.0))


# In[56]:

from pyspark.sql import SQLContext
sqlCtx=SQLContext(sc)


# In[57]:

trainDf=sqlCtx.createDataFrame([
    (1.0, Vectors.dense([0.0, 1.1, 0.1])),
    (0.0, Vectors.dense([2.0, 1.0, 1.0])),
    (0.0, Vectors.dense([2.0, 1.3, 1.0])),
    (1.0, Vectors.dense([0.0, 1.2, 0.5]))], ["label","features"]                    


# 1130

# In[58]:

from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector
_rdd = sc.parallelize([
    (0.0, SparseVector(4, {1: 1.0, 3: 5.5})),
    (1.0, SparseVector(4, {0: -1.0, 2: 0.5}))])


# In[60]:

from pyspark.mllib.linalg import SparseVector, VectorUDT
from pyspark.mllib.linalg import SparseVector
_rdd = sc.parallelize([
    (0.0, SparseVector(4, {1: 1.0, 3: 5.5})),
    (1.0, SparseVector(4, {0: -1.0, 2: 0.5}))])


# In[61]:

schema = StructType([
    StructField("label", DoubleType(), True),
    StructField("features", VectorUDT(), True)
])


# In[ ]:

trainDf=_rdd.toDF(schema)


# ## libsvm

# In[ ]:

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)


# In[ ]:

svmfn="C:\Users\LG-PC\Downloads\spark-1.6.0-bin-hadoop2.6\spark-1.6.0-bin-hadoop2.6\data\mllib\sample_libsvm_data.txt"
svmDf = sqlCtx.read.format("libsvm").load(svmfn)


# In[ ]:

print svmfn


# In[ ]:

svmDf.printSchema()


# In[ ]:

svmDf.take(1)


# word vector : 단어가 문장을, 문장이 문서를 만들 때, 단어의 순서가 의미가 없도록 하는 것이 bag or words. 단어별로 빈도를.

# In[ ]:

get_ipython().run_cell_magic(u'writefile', u'src/spark_wiki.txt', u"Wikipedia\nApache Spark is an open source cluster computing framework.\n\uc544\ud30c\uce58 \uc2a4\ud30c\ud06c\ub294 \uc624\ud508 \uc18c\uc2a4 \ud074\ub7ec\uc2a4\ud130 \ucef4\ud4e8\ud305 \ud504\ub808\uc784\uc6cc\ud06c\uc774\ub2e4.\nOriginally developed at the University of California, Berkeley's AMPLab,\nthe Spark codebase was later donated to the Apache Software Foundation,\nwhich has maintained it since.\nSpark provides an interface for programming entire clusters with\nimplicit data parallelism and fault-tolerance.")


# In[ ]:

lines = sc.textFile("src/spark_wiki.txt")


# In[ ]:

wc=lines.flatMap(lambda x:x.split())


# In[ ]:

wc.collect()


# In[ ]:

from operator import add
wc = sc.textFile("src/spark_wiki.txt")    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())    .map(lambda x:x.split())    .map(lambda x:[(i,1) for i in x])


# In[ ]:

for e in wc.collect():
    print e


# ## JSON을 SQL로

# In[ ]:

pDF=sqlCtx.read.json("C:/Users/LG-PC/Downloads/spark-1.6.0-bin-hadoop2.6/spark-1.6.0-bin-hadoop2.6/examples/src/main/resources/people.json")


# In[ ]:

type(pDF)


# In[ ]:

pDF.filter(pDF['age'] > 21).show()


# In[ ]:

pDF.registerTempTable("people")


# In[ ]:

sqlCtx.sql("select name from people").show()


# ## json from url

# In[ ]:

import requests
r=requests.get("https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json")


# In[ ]:

wc=r.json()


# In[ ]:

type(wc)


# In[ ]:

help()


# In[ ]:

wcDf=sqlCtx.createDataFrame(wc)


# In[ ]:

wcDf.printSchema()


# In[ ]:

wcDf.registerTempTable("wc")


# In[ ]:

sqlCtx.sql("select Club,Team,Year from wc").show()


# ## 1207

# ## s9. 정량데이터분석

# In[62]:

df = sqlCtx.createDataFrame(
    [
        ['No','young', 'false', 'false', 'fair'],
        ['No','young', 'false', 'false', 'good'],
        ['Yes','young', 'true', 'false', 'good'],
        ['Yes','young', 'true', 'true', 'fair'],
        ['No','young', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'good'],
        ['Yes','middle', 'true', 'true', 'good'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'good'],
        ['Yes','old', 'true', 'false', 'good'],
        ['Yes','old', 'true', 'false', 'excellent'],
        ['No','old', 'false', 'false', 'fair'],
    ],
    ['cls','age','f1','f2','f3']
)


# In[63]:

df.printSchema()


# In[64]:

from pyspark.ml.feature import StringIndexer
labelIndexer = StringIndexer(inputCol="cls", outputCol="labels")
model=labelIndexer.fit(df)


# In[65]:

df1=model.transform(df)


# In[66]:

df1.printSchema()


# In[67]:

df1.show()


# In[68]:

labelIndexer = StringIndexer(inputCol="age", outputCol="att1")
model=labelIndexer.fit(df1)
df2=model.transform(df1)


# In[69]:

labelIndexer = StringIndexer(inputCol="f1", outputCol="att2")
model=labelIndexer.fit(df2)
df3=model.transform(df2)


# In[70]:

labelIndexer = StringIndexer(inputCol="f2", outputCol="att3")
model=labelIndexer.fit(df3)
df4=model.transform(df3)


# In[71]:

labelIndexer = StringIndexer(inputCol="f3", outputCol="att4")
model=labelIndexer.fit(df4)
df5=model.transform(df4)


# In[72]:

df5.printSchema()


# In[73]:

df5.show()


# In[76]:

from pyspark.mllib.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

va = VectorAssembler(inputCols=["att1","att2","att3","att4"],outputCol="features")
df6 = va.transform(df5)


# In[77]:

df7=df6.withColumnRenamed('labels','label')


# In[78]:

df7.printSchema()


# In[79]:

trainDf=df7.select('label','features')


# In[80]:

trainDf.printSchema()


# In[81]:

trainDf.show()


# In[82]:

from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(maxIter=10, regParam=0.01)
model1 = lr.fit(trainDf)
print model1.coefficients
print model1.intercept


# In[ ]:

from pyspark.sql import Row
test0 = sc.parallelize([Row(features=Vectors.dense(2,0,0,1))]).toDF()
result = model1.transform(test0).head()


# ## s10. 텍스트분석

# In[83]:

from pyspark.ml.feature import HashingTF, IDF, Tokenizer, RegexTokenizer
from pyspark.sql import SQLContext

sqlCtx = SQLContext(sc)
df = sqlCtx.createDataFrame(
    [
        [0,'my dog has flea problems. help please.'],
        [1,'maybe not take him to dog park stupid'],
        [0,'my dalmation is so cute. I love him'],
        [1,'stop posting stupid worthless garbage'],
        [0,'mr licks ate my steak how to stop him'],
        [1,'quit buying worthless dog food stupid'],
        [0,u'우리 강아지 벌레 있어요 도와주세요'],
        [0,u'우리 강아지 귀여워 너 사랑해'],
        [1,u'강아지 공원 가지마 바보같이'],
        [1,u'강아지 음식 구매 마세요 바보같이']
    ],
    ['cls','sent']
)


# In[84]:

df.printSchema()


# In[85]:

tokenizer = Tokenizer(inputCol="sent", outputCol="words")


# In[86]:

tokDf = tokenizer.transform(df)


# In[87]:

tokDf.printSchema()


# In[88]:

for r in tokDf.select("cls", "sent").take(3):
    print(r)


# In[89]:

tokDf.show()


# In[90]:

re = RegexTokenizer(inputCol="sent", outputCol="wordsReg", pattern="\\s+")
regDf=re.transform(df)
regDf.show()


# ## Stop words
# 처리하지 말아야 하는 단어

# In[91]:

from pyspark.ml.feature import StopWordsRemover
stop = StopWordsRemover(inputCol="words", outputCol="nostops")


# In[92]:

stopwords=list()

_stopwords=stop.getStopWords()
for e in _stopwords:
    stopwords.append(e)


# In[93]:

_mystopwords=[u"나",u"너", u"우리"]
for e in _mystopwords:
    stopwords.append(e)


# In[94]:

stop.setStopWords(stopwords)


# In[95]:

for e in stop.getStopWords():
    print e,


# In[96]:

stopDf=stop.transform(tokDf)
stopDf.show()


# ## CountVectorizer

# In[97]:

from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'UNC played Duke in basketball',
    'Duke lost the basketball game'
]
vectorizer = CountVectorizer()
print vectorizer.fit_transform(corpus).todense()
print vectorizer.vocabulary_


# In[98]:

from pyspark.ml.feature import CountVectorizer
cv = CountVectorizer(inputCol="nostops", outputCol="cv", vocabSize=30,minDF=1.0)
cvModel = cv.fit(stopDf)
cvDf = cvModel.transform(stopDf)

cvDf.collect()
cvDf.select('words','nostops','cv').show()


# In[99]:

cvDf.select('cv').take(13)


# In[100]:

for v in cvModel.vocabulary:
    print v,


# ## StringIndexer

# In[101]:

from pyspark.ml.feature import StringIndexer
labelIndexer = StringIndexer(inputCol="cls", outputCol="labels")
model=labelIndexer.fit(cvDf)
trainDf2=model.transform(cvDf)


# In[102]:

trainDf2.printSchema()


# In[103]:

from pyspark.sql.functions import udf

toDoublefunc = udf(lambda x: x.DoubleType())
trainDf3 = trainDf2.withColumn("_label",toDoublefunc(trainDf2.cls))


# In[104]:

trainDf3.printSchema()


# In[ ]:




# ## S-13: spark-submit

# In[105]:

pwd


# In[106]:

get_ipython().run_cell_magic(u'writefile', u'src/spark_hello.py', u'print "---------BEGIN-----------"\nimport pyspark\nconf = pyspark.SparkConf().setAppName("myAppName1")\nsc   = pyspark.SparkContext(conf=conf)\nsc.setLogLevel("ERROR")\nprint "---------RESULT-----------"\nprint sc\nrdd = sc.parallelize(range(1000), 10)\nprint "mean=",rdd.mean()\nnums = sc.parallelize([1, 2, 3, 4])\nsquared = nums.map(lambda x: x * x).collect()\nfor num in squared:\n    print "%i " % (num)')


# 명령창에서
# .\spark-submit spark_hello.py
