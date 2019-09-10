import DataParser
import DataUtils
import NetworkAccess
import GetUrl

if __name__ == "__main__":
    CreateTable = True
    for i in range(0, 249, 25):
        url = GetUrl.Get_Data_Url(i)
        html_data = NetworkAccess.GetDataUrl(url)
        infoes = DataParser.Get_page_content(url, 0, html_data)
        if infoes == 0:
            pass
        else:
            item_list = DataUtils.ItemUtils()
            for i in range(len(infoes)):
                item_list.append(infoes[i]["name"], infoes[i]["content"], infoes[i]["score"], infoes[i]["say"])
                pass
           # item_list.clear()

            pass
        pass
    item_list.save_excel(sheet="表", file="list.xlsx")
    item_list.save_database(CreateTable)
    pass
