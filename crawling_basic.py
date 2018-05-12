from bs4 import BeautifulSoup
import urllib.request as req
def find():
    local=input("지역")
    date=input("날짜")
    time=input("시간")
    temp_data=data[local]
    for i in temp_data:
        if i[0]==date and i[1]==time:
            print(i[2:])
        else:
            pass

url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
soup=BeautifulSoup(req.urlopen(url).read(),"html.parser")
test=soup.find_all('data')
city=soup.find_all('city')
temp=[]
city_list=[]
data={}
for word in city:
    city_list.append(word.get_text())
    data[word.get_text()]=[]

for i in test:
    temp.append(i.get_text()[1:-1].split()[1:])
cnt=-1
for i in temp:
    if temp[0][0]==i[0] and temp[0][1]==i[1]:
        cnt+=1
    data[city_list[cnt]].append(i)
print(data)
find()



