import http.client
import urllib.request
print('开始')
request_url = 'http://192.168.7.33:84/PublicOpinion/PublicOpinionAjaxAPI.asmx/AddTpboLog'

headers = {
'content-Type':'application/x-www-form-urlencoded'
}

param={'SITE_NAME': 'hello','SITE_URL':'123','LOG_CONTENT':'222'}
data = urllib.parse.urlencode(param).encode(encoding='UTF8')

req = urllib.request.Request(request_url, headers=headers,data=data)

res = urllib.request.urlopen(req)
print(res.code)
if res.code == 200:
    tmpdata = res.read()
    tmpdata = str(tmpdata, 'utf-8')
    print(tmpdata)