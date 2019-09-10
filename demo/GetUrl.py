
url="https://movie.douban.com/top250?start=%d&filter="

def Get_Data_Url(p):
        url_page = url%p
        print(url_page)
        return url_page

if __name__ == '__main__':

    for i in range(0, 249, 25):
        p = i
        Get_Data_Url(p)
        pass

    pass
