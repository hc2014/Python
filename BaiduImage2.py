import http.client
import urllib.request
import json
import re
import os
import random
class BaiduImage(object):
    def __init__(self):
        super(BaiduImage,self).__init__()
        self.page=30
        if not os.path.exists(r'./image'):
            os.mkdir(r'./image')

    def download(data):
        for d in data:
            urllist =d['replaceUrl']
            for dd in urllist:
                try:
                    url=dd['ObjURL']
                    res = urllib.request.urlopen(url).read()
                    pattern = re.compile(r'.*/(.*?)\.jpg', re.S)
                    item = re.findall(pattern, url)
                    fileName = str('image/') + item[0] + str('.jpg')
                    with open(fileName, 'wb') as f:
                        f.write(res)
                except Exception as e:
                    continue

    def request(self):
        for i in range(1, 11):
            try:
                    request_url='http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%B5%B7%E8%B4%BC%E7%8E%8B%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E6%B5%B7%E8%B4%BC%E7%8E%8B%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn='+str(self.page)+'&rn=30&gsm=1e&1519803762360'

                    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36','Content':'test/json','refresh':'http://image.baidu.com'}
                    req = urllib.request.Request(request_url, headers=headers)
                    #req.add_header('refresh','image.baidu.com')
                    res= urllib.request.urlopen(req)
                    print(request_url)
                    print(str(res.code))
                    if res.code == 200:
                        data = res.read()
                        data=str(data,'utf-8')
                        data = json.loads(data)
                        BaiduImage.download(data['data'])

            except Exception as e:
                print('错误信息:'+str(e))
                continue
            finally:
                self.page += 30

if __name__ == '__main__':
        bi = BaiduImage()
        bi.request()
        print(str('下载完毕'))