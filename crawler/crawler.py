# encoding:utf-8

# import Queue
# initial_page = "http://dynamii.org"

# url_queue = Queue.Queue()
# seen = set()

# seen.insert(initial_page)
# url_queue.put(initial_page)

import urllib.request

url = "http://dynamii.org"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)