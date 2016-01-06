# coding = UTF-8
import urllib.request as ur
import re

# open the url and read
def getHtml(url):
    page = ur.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\..*)'
    url_re = re.compile(reg)

    # print(url_re)

    url_lst = url_re.findall(str(html))
    print(url_lst)
    obfile.write('\n'.join(url_lst))
    obfile.write('\n')
    obfile.close()
    return(url_lst)

# 1. 批量抓取站内的文件. 形成一个列表, 然后送给迅雷等专业下载软件处理.

raw_url = "http://delftxdownloads.tudelft.nl/aero/Week04/"
html = getHtml(raw_url)
# print(html)
obfile = open('url.txt','a+')
url_list = getUrl(html)

