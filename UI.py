from Crawling_weather_class import weather_midterm,local_weather

def mid_weather_print(weather):
    data= weather.data[weather.city_find]
    for date in data.keys():
        print(
'''
날짜 %s         
날씨:%s         
최저기온:%s     
최고기온:%s      
신뢰도:%s               
'''%(date,data[date][0],data[date][1],data[date][2],data[date][3]),end="--------------------------------------------------")


def local_weather_print(weather):

    data=weather.data
    for date in data.keys():
        day=date[:8]
        time=date[9:]

        print(
'''
시간:%s %s

평균 기온:%s
최고 기온:%s
최저 기온:%s
기상 상황:%s
강수 상태:%s
날씨:%s
Weather:%s
강수 확룰:%s
    
'''%(day , str(int(time)-3)+"~"+time ,data[date][0],data[date][1],data[date][2],data[date][3],data[date][4],data[date][5],data[date][6],data[date][7]),end="--------------------------------------------------")





mid_weather=weather_midterm("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
b=local_weather("http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=4146554000")
local_weather_print(b)