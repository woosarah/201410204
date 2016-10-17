import os
KEY="49756971476179613539737a456442"
TYPE='json'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'
params=os.path.join(KEY, TYPE, SERVICE,START_INDEX,END_INDEX,LINE_NUM)
url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=LINE_NUM
myurl='http://openapi.seoul.go.kr:8088/49756971476179613539737a456442/xml/SearchSTNBySubwayLineService/1/5/1/'
import requests
data=requests.get(myurl)
print data.text