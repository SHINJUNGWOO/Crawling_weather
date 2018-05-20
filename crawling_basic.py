from Crawling_weather_class import weather_midterm,local_weather
from UI import screen as sc
import os
import datetime as dt
#from Step_move import easydriver



mid_weather=weather_midterm("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
local_weather=local_weather("http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=4146554000")

#step=easydriver(18, 0.004, 23, 24, 17, 25)
#only use in raspberry

screen=sc(mid_weather,local_weather)
run=True

os.system('cls')


while(run):
    if screen.screen_code==0:
        screen.first_screen()
    elif screen.screen_code==1:
        screen.mode_select()
    elif screen.screen_code==2:
        screen.weather_Inpormation()
    elif screen.screen_code == 3:
        screen.Time_Select()
    else:
        run=False


