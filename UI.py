import os
import datetime
class screen:
    def __init__(self,mid_weather,local_weather):
        self.mid_weather=mid_weather
        self.local_weather=local_weather
        self.mode=0
        self.mode_dir = {0: 'Auto Mode', 1: 'Time Mode', 2: 'Test Mode'}
        self.screen_code=4
        self.day_selected=None
        self.time_selected=None
# screen code{1:mode select screen , 2:Weather Impormation ,3: time select, 4:Condition}
# mode number {0=Auto,1:Timemode 2:TestMode}
    def first_screen(self):
        print('''
        Blind Automatic move System:
        ---------------------------------------
        - (M)Mode Select                      -
        -                                     -
        - (W)Weather Impormation              -
        -                                     -
        - (T)TIme Select                      -
        -                                     -
        _ (C)Condition                        -
        -                                     -
        _ (A)Manual Control                   - 
        --------------------------------------- 
        ''')
        cnt_check=input("Input:")
        if cnt_check=='M'or cnt_check=='m':
            self.screen_code=1
        elif cnt_check=='W'or cnt_check=='w':
            self.screen_code=2
        elif cnt_check == 'T' or cnt_check == 't':
            self.screen_code=3
        elif cnt_check == 'C' or cnt_check == 'c':
            self.screen_code=4
        elif cnt_check == 'A' or cnt_check == 'a':
            self.screen_code=5
        else:
            self.screen_code=0
        os.system('cls')

    def mode_select(self):

        print('''
        Blind Automatic move System:
        ---------------------------------------
        -                                     -
        - Recent Mode=%s               -
        -                                     -
        ---------------------------------------
        - (A)Auto Mode                        -
        -                                     -
        - (T)Time Mode                        -
        -                                     -
        _ (E)Test Mode                        - 
        --------------------------------------- 
            '''%(self.mode_dir[self.mode]))
        cnt_check=input("Input:")
        if cnt_check=='A'or cnt_check=='a':
            self.mode=0
            self.screen_code = 4
        elif cnt_check=='T'or cnt_check=='t':
            self.mode=1
            self.screen_code = 4
        elif cnt_check == 'E' or cnt_check == 'e':
            self.mode=2
            self.screen_code = 4
        else:
            self.screen_code=1
        os.system('cls')

    def weather_Inpormation(self):
        print('''
        Blind Automatic move System:
        ---------------------------------------
        - (L)Local Forecast                   -
        -                                     -
        - (M)Midterm Forcast                  -
        --------------------------------------- 
            ''')
        cnt_check=input("Input:")
        if cnt_check=='L'or cnt_check=='l':
            os.system('cls')
            self.local_weather_print()
            input("\n\tPress Any Key:")
            self.screen_code=4
            os.system('cls')
        elif cnt_check=='M'or cnt_check=='m':
            os.system('cls')
            self.mid_weather_print()
            input("\n\tPress Any Key:")
            self.screen_code=4
            os.system('cls')
        else:
            self.screen_code=4
            os.system('cls')

    def Time_Select(self):
        if self.mode !=0 and self.mode !=1:
            self.screen_code=1
        elif self.mode ==2:
            os.system('cls')
            self.day_selected=input("Select day")
            self.time_selected = input("Select time")
        else:
            os.system('cls')
            print('''
        Blind Automatic move System:
        ---------------------------------------
        -                                     -
        - Recent Mode=%s               -
        ---------------------------------------        
        -                                     -
        - Recent Day=%s              
        - Recent Time=%s
        -                                     -
        --------------------------------------- 
        - (D)Day Select                       -
        -                                     -
        - (T)Time Select                      -
        -                                     -
        --------------------------------------- 
            '''%(self.mode_dir[self.mode],self.day_selected,self.time_selected))

            cnt_check = input("Input:")
            if cnt_check == 'D' or cnt_check == 'd':
                os.system('cls')
                print('''
        Blind Automatic move System:
        ---------------------------------------
        --------------------------------------- 
        - Select Day=YYYY-MM-DD               -
        -                                     -
        - None Select Day=None                -
        -                                     -
        --------------------------------------- 
                    ''')
                dnt_check=""
                try:
                    dnt_check=input("Input:")
                    datetime.datetime.strptime(dnt_check, '%Y-%m-%d')
                except:
                    if dnt_check==None:
                        self.day_selected=None
                    else:
                        self.screen_code=3
                else:
                    self.day_selected=dnt_check
            elif cnt_check == 'T' or cnt_check == 't':
                os.system('cls')
                print('''
        Blind Automatic move System:
        ---------------------------------------
        --------------------------------------- 
        - Select TIme= HH-MM                  -
        -                                     -
        - None Select TIME=None               -
        -                                     -
        --------------------------------------- 
                    ''')
                dnt_check=""
                try:
                    dnt_check=input("Input:")
                    datetime.datetime.strptime(dnt_check, '%H-%M')
                except:
                    if dnt_check==None:
                        self.time_selected=None
                    else:
                        self.screen_code=3
                else:
                    self.time_selected=dnt_check
            else:
                os.system('cls')
                self.screen_code=4

    def Condition(self):
        local_data=self.local_weather.data[self.local_weather.date_list[0]]
        # Fisrt data of local_weather_data
        os.system("cls")
        print('''
        Blind Automatic move System:
        ---------------------------------------
        -Resent Time:%s
        ---------------------------------------
        평균 기온 : %s
        
        강수 상태 :%s
        
        날씨 : %s
        ---------------------------------------
        -Setting(Keyboard Interrupt(CTRL+C))  -
        --------------------------------------- 
        '''%(datetime.datetime.now().strftime("%Y-%m-%d   %H:%M:%S"),local_data[0],local_data[4],local_data[5]))

    def ManualMove(self):
        print('''
        Blind Automatic move System:
        ---------------------------------------
        - (U)UP                               -
        -                                     -
        - (D)DOWN                             -

        --------------------------------------- 
        ''')
    def mid_weather_print(self):
        weather=self.mid_weather
        data= weather.data[weather.city_find]
        for date in data.keys():
            print(
    '''
    날짜 %s
    ---------------------------------------      
    날씨 : %s         
    최저기온 : %s     
    최고기온 : %s      
    신뢰도 : %s               
    '''%(date,data[date][0],data[date][1],data[date][2],data[date][3]),end="---------------------------------------")


    def local_weather_print(self):
        weather=self.local_weather
        data=weather.data
        for date in data.keys():
            day=date[:8]
            time=date[9:]

            print(
    '''
    시간:%s %s
    ---------------------------------------
    평균 기온 : %s
    최고 기온 : %s
    최저 기온 : %s
    기상 상황 : %s
    강수 상태 : %s
    날씨      : %s
    Weather   : %s
    강수 확룰 : %s
        
    '''%(day , str(int(time)-3)+"~"+time ,data[date][0],data[date][1],data[date][2],data[date][3],data[date][4],data[date][5],data[date][6],data[date][7]),end="---------------------------------------")






#Test line
# mid_weather=weather_midterm("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
# b=local_weather("http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=4146554000")
