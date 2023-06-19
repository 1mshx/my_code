import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Accept': ' */*',
    'Accept-Encoding': ' gzip, deflate, br',
    'Accept-Language': ' zh-CN,zh;q=0.9',
    'Acs-Token': ' 1684726227237_1684726279281_fs8sdMdEDttG1CYHTK0VwoYjwKWDJZNzRdSLG7EvWLGdzPLQftRGqTiT0fBuK3693bHgEJE+TQpBbGaicJBttcqsbZ3mms2mxBdphqe+4Pe8VQgKHgNodf1r9pLiK6X21o4WXrU75UbZR/zBFFKx0h9tZTFJeHjFi8BgdDvjdIMr6dol4OT+6mHd9mW2s1+odzxBXEDMSKGfEnD9b8BnHtTyRh//WcHIYHWUGBc9U9DLLIrkkvkov2zp/rIfVFpgQDS0exIDTGnw2i03lTAIUSjFdOiartExGUrnueERpD/m2piyHQjn22e6SdUwavHPj6ggVdf/86SpmWy+7nabp4CuMD4NQUEjMJIrl+dBzXMMe+oarPX3ep0B3tKo4tnwfbp1ji33vnBqjAPvPp44kOXHD/swzVUF1lMvU/p67Mgdf5kOPhawGeh7yhZxCUP8iqcmSD6vqAAlucOTQCKJIxBFiDhLRg2aWhFTdo5ZoaE=',
    'Connection': ' keep-alive',
    'Content-Length': ' 153',
    'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': ' BIDUPSID=E98B5FC90B234DF3CE02307E6B086E5A; PSTM=1679145127; BAIDUID=85009BF39C4EB5011C4A3F3ED64233F2:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID_BFESS=85009BF39C4EB5011C4A3F3ED64233F2:FG=1; ZFY=zCs5GyKipLFUqP237:Ac8mfjlbDQNVj0gvLinNltTth0:C; H_PS_PSSID=38516_36553_38617_38538_38594_38576_38414_38637_26350_38619_38667; BA_HECTOR=8g84a1ak2h20848h25akal691i6llfr1n; PSINO=6; delPer=0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1684230657,1684307259,1684723227; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1684726227; ab_sr=1.0.1_NDk1NGQ3ODk0YWMzN2FjMzc4NjA3Y2QwZDY3ZmQwNzQ3MDhkNTVlMTI2NmU0NGQxYTI5MjM4M2M1ZWI1ODUwNjdkM2JmZmMzNDMyYzU5MTFmYzcwN2NhNzc4MmZkMWFhMTNkNzMzNDdmZTBmNWE1ZmU0ZDY4YTM1YjQ0YjRlMDc3ZmU2NzFlZmFkNTE4NTRkYWYzNjQ0YzFiNjdjNWQ0Yg==',
    'Host': ' fanyi.baidu.com',
    'Origin': ' https://fanyi.baidu.com',
    'Referer': ' https://fanyi.baidu.com/?aldtype=16047',
    'Sec-Fetch-Dest': ' empty',
    'Sec-Fetch-Mode': ' cors',
    'Sec-Fetch-Site': ' same-origin',
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'X-Requested-With': ' XMLHttpRequest',
    'sec-ch-ua': ' "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"'
}
