
import pymysql
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

db = pymysql.connect(host="localhost", user="root", password="zh19941221", db="readish", port=3306)
cursor = db.cursor()
db.set_charset('utf8')


def insertdata(title, picurl, url):
    sql_insert = "insert into chinadaily (newstitle,newspictureurl,newsurl) values('%s','%s','%s')"
    try:
        cursor.execute(sql_insert % (title, picurl, url))
        db.commit()
        print("插入数据成功")
    except pymysql.Error as e:
        db.rollback()
        print("插入数据失败")


def imagesource (url):
    imageurl = requests.get(url, headers=headers)
    imagesoup = BeautifulSoup(imageurl.text, 'lxml')
    if imagesoup.find("figure") != None :
        return imageSoup.find("figure").find("img").attrs['src']


data = []

r = requests.get("http://www.chinadaily.com.cn/", headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
for element in soup.find_all(attrs={'class':'cmLBoxR'}):
    for each in element.find_all('a'):
        newstitle = each.string
        newspicurl = each.attrs['href']
        newsurl = imageSource(each.attrs['href'])
        if newstitle != None and newspicurl != None and newsurl != None:
            obj = {'title': newstitle, 'url': newsurl, 'image': newspicurl}
            newstitle = str(newstitle)
            newspicurl = str(newspicurl)
            newsurl = str(newsurl)
            print(newstitle, newspicurl, newsurl)
            insertData(newstitle, newspicurl, newsurl)
            data.append(obj)
            
print(data)
db.close()
