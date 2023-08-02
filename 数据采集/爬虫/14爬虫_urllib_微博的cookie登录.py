# 使用的场景:数据采集的时候，需要绕过登录 然后进入到某个页面

import urllib.request

url = 'https://weibo.com/u/page/follow/7848081846'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
    'Cookie': 'SINAGLOBAL=9214440961648.527.1687614031638; XSRF-TOKEN=KntlQj_Y_oInkVZSIEGQjDDO; '
              'login_sid_t=e604bb672a2280aaf0ff2ab1f7a8074a; cross_origin_proto=SSL; _s_tentry=weibo.com; '
              'Apache=2907061199030.685.1690943635582; '
              'ULV=1690943635584:2:1:1:2907061199030.685.1690943635582:1687614031642; wb_view_log=1536*8641.25; '
              'SSOLoginState=1690943871; '
              'SCF=AjWi3iwCLoI3ggjuvtvulTvKkfJHOD3AGgNPHhMX1xDwDykD00YaJvsrOcgBAmVRyzwOAstnDuZ3qnYjrXPS4bg.; '
              'SUB=_2A25JzbHQDeRhGeFG71oR-C_EzzqIHXVquqQYrDV8PUNbmtANLU_HkW9NeX2XX4Q1lXtGFY63aK43kL54C_y_sxJw; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWTxqC15cbhDEecIVdTJLwr5JpX5KzhUgL'
              '.FoMRShn71h2RShq2dJLoIEnLxKqL1KqL1hMLxKqL1KnL12-LxKBLBonL122LxKMLB.BL1K2Eeh5E; ALF=1722479871; '
              'PC_TOKEN=252acc9c4c; '
              'WBPSESS'
              '=cUL_kn_lmoA4A4AGAONHaB9B4rI9y8d8fIZwXohBGyF_wM6WGkBYMbZqgNYIVJAbpN0_bvOGiEmJD8GnoiaV3Li1FjFGTS2vrtpXGIhPO-sOKCeiUSGXR9WhVpQbl1Mnoqb9g6DaYnIdAqkbnl9GoA==',
    # 'Referer': 'https://weibo.com/u/page/follow/7848081846',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

with open('爬取内容/微博.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
