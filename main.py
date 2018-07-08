from GetID_Douban import Douban_id
from getComments import getComments
from Keywords import keywords

if __name__ == '__main__':

    name = input("input name:")
    sort = input("input sort('music','movie','book'):")
    id = Douban_id(name=name,sort=sort).getID()
    #print(id)
    filePath = getComments(name=name,id=id,sort=sort)
    keywords(filePath)
    print("已完成！")
    print("请在评论信息文件夹中查看。")
