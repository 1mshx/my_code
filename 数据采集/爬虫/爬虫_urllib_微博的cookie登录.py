# 使用的场景:数据采集的时候，需要绕过登录 然后进入到某个页面

import urllib.request

url = 'https://weibo.com/u/7848081846'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('gb2312')

print(content)

with open('爬取内容/微博.html', 'w', encoding='gb2312') as fp:
    fp.write(content)

