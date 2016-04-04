import urllib
import urllib.request

# ##################################
# 向百度搜索一些关键词
# ##################################

# 存储搜索用的关键词
data = {}
data['word'] = 'Jecvay Notes'

query_word = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + query_word

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')      # 这句话有问题。。。。
print(data)