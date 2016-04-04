# 试试抓取知乎的数据
import urllib.request
url = "https://www.zhihu.com/collection/36644506"
data = urllib.request.urlopen(url).read()
print(data.decode('gbk', errors='ignore'))