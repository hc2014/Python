#根据代理IP给网站刷流量
import urllib.request
import urllib.error
import random
import socket
#创建get方法
def get(url,ip):

 proxy_support = urllib.request.ProxyHandler({"http":ip})
 opener = urllib.request.build_opener(proxy_support)

 headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
 urllib.request.install_opener(opener)

 req = urllib.request.Request(url, headers=headers)
 return urllib.request.urlopen(req).code
if __name__ == '__main__':

#代理IP，这个可以去必读找可用代理IP
 proxies=['112.254.181.4:8118',
'110.73.53.104:8123',
'122.114.31.177:808',
'61.135.217.7:80']
url = "https://www.qiushibaike.com/hot/page/1/"

socket.setdefaulttimeout(2)

 #记录次数
for ip in proxies[::-1]:
    try:
        code = get(url, ip)
        print('访问成功:' + str(ip))
    except Exception as e:
        #proxies.remove(ip)
        print('错误IP:'+str(ip)+"错误信息:"+str(e))
        continue
print('执行完毕')





