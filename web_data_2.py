import urllib2
url='http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data'
res=urllib2.urlopen(url)
html = res.read()
res.close()
print len(html)
lines=html.splitlines()
data=[]
for line in lines:
    data.append(line.split())
print len(data), len(data[0])
print data[0]