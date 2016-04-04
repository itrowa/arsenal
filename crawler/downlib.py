import urllib.request
import os
import re

from bs4 import BeautifulSoup

def url_open(url):
    """ 根据URL返回该地址的资源。
    """
    # init a request obj
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')

    # urlopen method需要一个request对象作为参数。
    response = urllib.request.urlopen(req)

    if response.getcode() == 200:
        return response.read()
    else:
        print("error open url ", url)


url = "http://dynamii.org/"

# with open("resource.txt", "w", encoding="utf-8") as f:
#     f.write(url_open(url).encode("UTF-8"))

# 记得要先从utf8解码出来。
t = url_open(url).decode('utf8')

soup = BeautifulSoup(t, 'html.parser', from_encoding="utf8")

result = soup.find_all('ul') 

f = open("Resource.txt", "w", encoding="utf-8")
f.write(t)
f.close()