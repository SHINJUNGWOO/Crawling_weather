from bs4 import BeautifulSoup
import urllib.request as req
import datetime

class weather_midterm:
    def __init__(self,url,city_find="서울",date_find=datetime.datetime.today().strftime("%Y-%m-%d")):
        self.soup = BeautifulSoup(req.urlopen(url).read(), "html.parser")
        self.city_list = []
        self.date_list=[]
        self.data = {}
        self.make_data()
        self.city_find=city_find
        self.date_find=date_find
    def make_data(self):
        temp_weather=self.soup.find_all('data')
        temp_city= self.soup.find_all('city')
        city_list=[]
        data_dir={}
        for city in temp_city:
            city_list.append(city.get_text())
            data_dir[city.get_text()]=[]

        temp_list=[]

        for weather in temp_weather:

            temp_list.append(weather.get_text()[1:-1].split()[1:])


        cnt = -1
        for i in temp_list:
            if temp_list[0][0] == i[0] and temp_list[0][1] == i[1]:
                cnt += 1
            data_dir[city_list[cnt]].append(i)

    # city- dic making

        for data in data_dir[city_list[0]]:
            self.date_list.append(data[0])

        for city in city_list:
            temp_dir={}
            for data in data_dir[city]:
                if len(data[2:])==5:
                    data[2:]=[data[2]+" "+ data[3],data[4],data[5],data[6]]
                temp_dir[data[0]+" "+data[1]]=data[2:]
            data_dir[city]=temp_dir

        self.city_list=city_list
        self.data=data_dir
    def select_city(self,city):
        self.city_find=city


class local_weather:
    def __init__(self,url):
        self.soup = BeautifulSoup(req.urlopen(url).read(), "html.parser")
        self.data={}
        self.make_data()
    def make_data(self):
        cloud_dic = {'1': '맑음', '2': '구름 적음', '3': '구름 많음', '4': '흐림'}
        rainy_dic = {'0': '맑음', '1': '비', '2': '눈/비', '3': '눈'}
        time=self.soup.find_all("tm")[0].get_text()[:8]
        temp_weather=self.soup.find_all('data')
        temp_data=[]
        data_dir={}
        for i in temp_weather:
            temp_data.append(i.get_text().split("\n")[1:-10])
        for data in temp_data:
            data[5]=cloud_dic[data[5]]
            data[6]=rainy_dic[data[6]]
            data_dir[str(int(time)+int(data[1]))+" "+data[0]]=data[2:]
        self.data=data_dir
        #   (시간 -3~0,평균 온도,최고 기온,최저기온,하늘상태(1:맑음,2:구름 적음,3:구름 많음,4:흐림),강수상태(1:비,2:눈/비3:눈),한국어 날씨, 영어 날씨, 강수확률)


#----------------------------test-------------------------------------------------------------
a=weather_midterm("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
b=local_weather("http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=4146554000")
# TODO: 지역 날씨 처리 로직 작성, 데이터 처리