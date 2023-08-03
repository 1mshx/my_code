import urllib.request

url = 'https://www.ip.cn'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
    #           'application/signed-exchange;v=b3;q=0.7'
    # 'Cookie': 'BIDUPSID=E98B5FC90B234DF3CE02307E6B086E5A; PSTM=1679145127; '
    #           'BAIDUID=85009BF39C4EB5011C4A3F3ED64233F2:FG=1; BD_UPN=12314753; '
    #           'BDUSS_BFESS'
    #           '=dTWkljc0Z4UU9kTEhTQzk0ZnptOERFd29LcjkyS2JBLUpGeGFQcVNINXpSZGhrRUFBQUFBJCQAAAAAAAAAAAEA'
    #           'AADZCNpsz7K7ttChs8jX0zA0MjgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    #           'AAAAAAAAHO4sGRzuLBkMm; sugstore=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;'
    #           ' BA_HECTOR=81a580a5050gakalah8480ad1ick9v01o; delPer=0; BD_CK_SAM=1; PSINO=7; '
    #           'BAIDUID_BFESS=85009BF39C4EB5011C4A3F3ED64233F2:FG=1; ZFY=zCs5GyKipLFUqP237:'
    #           'Ac8mfjlbDQNVj0gvLinNltTth0:C; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1690970083;'
    #           ' Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1690970083; COOKIE_SESSION=1034089_1_9_9_4_17_0_0'
    #           '_9_8_1_1_45_0_0_0_1689935998_1689305428_1690970081%7C9%239829410_3_1689305405%7C2; BD_HOME=1; '
    #           'BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=36553_39108_38920_39114_39037_38917_39085_26350_'
    #           '39140_39101_39043; H_PS_645EC=a4d5Um5ujLn2vJK9o4i%2FaT2ijEXW73sdEnd0VYm21aODDsFK%2FuoQ8f99LNzpJED1YC8f; '
    #           'baikeVisitId=7ac2df1c-757e-452f-b632-fdef51c1d821; BDSVRTM=239'
}

# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

proxies = {
    'http': '103.237.78.102:4995'
}

# handler build_opener open
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应信息
content = response.read().decode('utf-8')

# 保存在本地
with open('爬取内容\daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
