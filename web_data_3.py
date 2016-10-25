import urllib
keyword='Python (programming language)'
s = urllib.urlopen('http://en.wikipedia.org/w/index.php?action=raw&title='+keyword).read()
#print s.find('Python is a widely used general-purpose')
print s[:5000]