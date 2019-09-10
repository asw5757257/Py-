import requests;
from bs4 import BeautifulSoup
import pymysql;
import os;
import time;
import locale
header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
def GetNowTime():
    locale.setlocale(locale.LC_CTYPE, 'chinese')
    newtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    t = time.strptime(newtime, "%Y-%m-%d %H:%M:%S")
    return time.strftime("%Y年%m月%d日%H时%M分%S秒", t)
    pass
dir_name = "访问记录"
def GetDataUrl(url):
    requests_url = requests.get(url,header)
    if requests_url.status_code == 200:
        html_data = requests_url.content.decode("utf-8")
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print("文件夹:'访问记录'创建成功")
            pass
        file = open("%s\%s.txt"%(dir_name,str(GetNowTime())),"w",1,encoding="utf-8")
        file.write(html_data)
        file.close()
        return html_data
        pass
    else:
        print("访问失败")
        print("失败状态码:",requests_url.status_code)
        return 0
        pass
    pass
