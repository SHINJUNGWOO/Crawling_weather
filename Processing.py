import datetime
import os


class processging:
    def __init__(self,screen,cds):
        self.screen=screen
        self.cds=cds
        self.day_selected=screen.day_selected
        self.time_selected=screen.time_selected
        self.now_day=datetime.datetime.now().strftime('%Y-%m-%d')
        self.now_time = datetime.datetime.now().strftime('%H-%M')
        self.condition=False
        self.fix=False
        #motor UP = True, motor Down = False
    def main_process(self,screen,cds):

        self.day_selected=screen.day_selected
        self.time_selected=screen.time_selected
        self.now_day=datetime.datetime.now().strftime('%Y-%m-%d')
        self.now_time = datetime.datetime.now().strftime('%H-%M')

        if self.screen.mode==0:
            self.auto_process()
        elif self.screen.mode == 1:
            self.time_process()
    def auto_process(self):
        tmp_time=""
        temp_now=self.now_day+"-"+self.now_time
        if self.time_selected !=None:
            if self.day_selected != None:
                tmp_time=self.day_selected+"-"+self.time_selected
            else:
                tmp_time=self.now_day+"-"+self.time_selected
        else:
            pass

        if tmp_time == temp_now:
            self.condition=True
            self.fix = True
        else:
            pass
        if self.fix==False:
            if self.cds.check():
                self.condition=False
            else:
                self.condition=True
        else:
            pass


    def time_process(self):
        self.fix=False
        tmp_time=""
        temp_now=self.now_day+"-"+self.now_time
        if self.time_selected !=None:
            if self.day_selected != None:
                tmp_time=self.day_selected+"-"+self.time_selected
            else:
                tmp_time=self.now_day+"-"+self.time_selected
        else:
            pass

        if tmp_time == temp_now:
            self.condition=True
        else:
            pass

    def manual_move(self,way):
        self.fix=False
        if self.screen.mode==0:
            os.system('cls')
            print('''
        Mode Error=(AutoMode)
        ''')
        else:
            if way==True:
                self.condition=True
            else:
                self.condition=False




