import http.client
import urllib.request
import json
import re
import os
class BaiduImage(object):
    def __init__(self):
        super(BaiduImage,self).__init__()
        self.page=60
        if not os.path.exists(r'./image'):
            os.mkdir(r'./image')

    def download(data):
        for d in data:
            try:
                url = d['objURL']
                res = urllib.request.urlopen(url).read()
                pattern = re.compile(r'.*/(.*?)\.jpg', re.S)
                item = re.findall(pattern, url)
                fileName = str('image/') + item[0] + str('.jpg')
                with open(fileName, 'wb') as f:
                    f.write(res)
            except Exception as e:
                print(str(e))
                continue

    def request(self):
        i=0
        try:
            while i<1:
                conn = http.client.HTTPConnection('image.baidu.com')
                request_url='/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&cg=girl&rn=60&pn=' + str( self.page)
                #request_url='search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E9%BB%84%E7%9F%B3'

                #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0','Content-type':'test/html'}
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36','Content':'test/html'}

                conn.request('GET',request_url,headers=headers)
                r=conn.getresponse()
                print(str(r.status))
                if r.status == 200:
                    data = r.read()
                    data=str(data,'utf-8')
                    data = json.loads(data)
                    BaiduImage.download(data['imgs'])
                    self.page+=60
                    i=1

        except Exception as e:
                print(e)
        finally:
            conn.close()

if __name__ == '__main__':
        bi = BaiduImage()
        bi.request()
        print(str('下载完毕'))