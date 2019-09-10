from bs4 import BeautifulSoup
import requests
def Get_page_content(url_page,i,requests_data):
    if requests_data == 0:
        return 0
        pass
    '''if i == 0:
        print("查询第一页内容，不用再次网络访问")
        pass
    else:
        # 网络访问
        requests_data =  Get_Data_Url(url_page);
        pass
        '''
    # 开始解析数据
    soup =BeautifulSoup(requests_data,"html.parser");
    div_all = soup.find_all("div",attrs={"class":"item"});
    #print(len(div_all));
    infoes=[]
    # 遍历每一条信息
    for div_item in div_all:
        # 1.1 电影名称
        name = div_item.find("span", attrs={"class": "title"}).string
        # 1.2 电影内容简述
        content = div_item.find("div", attrs={"class": "bd"}).find("p",attrs={"class":""}).text
        # 1.3 电影评分
        score = div_item.find("div", attrs={"class": "bd"}).find("span", attrs={"class": "rating_num"}).string
        # 1.4 电影主题
        temp = div_item.find("div", attrs={"class": "bd"}).find("span", attrs={"class": "inq"})
        if temp == None:
            say = "空"
            pass
        else:
            say = div_item.find("div", attrs={"class": "bd"}).find("span", attrs={"class": "inq"}).string
            pass
        # print("==========================================================================");
        # print("电影名称：",name);
        # print("电影内容简述：", content);
        # print("电影评分：", score);
        # print("电影主题：", say);
        #content = str(content)
       # content.replace("导","你")

        strs =  "".join(content.split())
        strs = strs.replace("'", ".")
        say = say.replace("'", ".")
       # print(strs)
        info={"name":name,"content":strs,"score":score,"say":say}
        infoes.append(info)
        pass

    '''for i in range(len(infoes)):
        print(infoes[i])
        pass
    '''

    return infoes
    pass
if __name__ == "__main__":

    pass
