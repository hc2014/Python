# 通过代理IP网站 抓取可用代理IP
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import socket

header = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

'''
获取所有代理IP地址
'''


def getProxyIp():
    proxy = []
    for i in range(1, 5):
        try:
            url = 'http://www.xicidaili.com/nn/' + str(i)
            req = urllib.request.Request(url, headers=header)
            res = urllib.request.urlopen(req).read()
            soup = BeautifulSoup(res)
            ips = soup.findAll('tr')
            for x in range(1, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                ip_temp = tds[1].contents[0] + "\t" + tds[2].contents[0]
                proxy.append(ip_temp)
        except Exception as e:
            print('错误1:')
            print(e)
            continue
    return proxy


'''
验证获得的代理IP地址是否可用
'''


def validateIp(proxy):
    url = "http://ip.chinaz.com/getip.aspx"
    f = open("E:\ip.txt", "w")
    socket.setdefaulttimeout(3)
    for i in range(0, len(proxy)):
        try:
            ip = proxy[i].strip().split("\t")
            proxy_host = "http://" + ip[0] + ":" + ip[1]
            f.write(proxy[i] + '\n')
        except Exception as e:
            print('错误2:')
            print(e)
            continue
    f.close()



if __name__ == '__main__':
    proxy = getProxyIp()
    validateIp(proxy)