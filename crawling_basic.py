from Crawling_weather_class import weather_midterm,local_weather
from UI import screen as sc
from CDS import CDS
from Processing import processging
import os
import time
import datetime as dt
#from Step_move import easydriver



mid_weather=weather_midterm("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
local_weather=local_weather("http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=4146554000")

#step=easydriver(18, 0.004, 23, 24, 17, 25)
#only use in raspberry

screen=sc(mid_weather,local_weather)
cds=CDS()
process=processging(screen,cds)
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
    elif screen.screen_code == 4:
        screen.Condition()
    elif screen.screen_code == 5:
        open_dir={True:"OPEN",False:"CLOSE"}
        screen.ManualMove()
        print('''
        ---------------------------------------
        - Recent Condition:%s 
        --------------------------------------- 
        '''%(open_dir[process.condition]))
        cnt_check=input("Input:")
        if cnt_check=='U' or cnt_check=='u':
            process.manual_move(True)
            screen.screen_code = 4
        elif cnt_check=='D' or cnt_check=='d':
            process.manual_move(False)
            screen.screen_code = 4
        else:
            os.system('cls')
            screen.screen_code=0
    else:
        run=False
    process.main_process(screen,cds)



    try:
        time.sleep(0.5)
    except:
        os.system("cls")
        screen.screen_code=0

