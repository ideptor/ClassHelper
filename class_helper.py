from tkinter import *
import time
import tkinter
from functools import partial
import webbrowser
import time
import threading
import datetime
import data_loader as loader
from playsound import playsound


class PlaySoud(threading.Thread):

    def __init__(self, repeat):
        super().__init__()
        self.repeat = repeat

    def run(self):
        for i in range(self.repeat):
            playsound('beep_1s.mp3')


class Alarm(threading.Thread):

    ALARM_COLOR = 'red'
    DEFAULT_COLOR = 'SystemButtonFace'
    ALARM_INTERVAL = 0.6
    
    ALARM_BLINK_DURATION_SEC = 5 * 60
    ALARM_PLAY_SOUND_DURATION_SEC = 5

    def __init__(self, label, index, enabled_list, start_time):
        super().__init__()
        self.setDaemon(True)
        self.label = label
        self.index = index
        self.enabled_list = enabled_list
        self.start_hour = int(start_time[0:2])
        self.start_min = int(start_time[3:5])
        self.played = False 

        if self.start_min >= 2:
            self.start_min -= 2
        else:
            self.start_hour -= 1
            self.start_min += 58


        print( self.start_hour, self.start_min)
    

    def run(self):
        
        cur_col = Alarm.ALARM_COLOR
        while True:
            if self.enabled_list[self.index] == True:

                now = datetime.datetime.now()
                start = now.replace(hour=self.start_hour, minute=self.start_min, second=0)
                diff_seconds = (now - start).total_seconds()
                
                if diff_seconds < 0 or diff_seconds >= Alarm.ALARM_BLINK_DURATION_SEC:
                    time.sleep(Alarm.ALARM_INTERVAL)
                    continue
                    
                if diff_seconds > 0 and self.played == False:
                    play = PlaySoud(5)
                    play.start()
                    self.played = True

                if cur_col == Alarm.ALARM_COLOR:
                    cur_col = Alarm.DEFAULT_COLOR
                else:
                    cur_col = Alarm.ALARM_COLOR
                self.label.config(bg=cur_col)

            else:
                #cur_col = Alarm.DEFAULT_COLOR
                self.label.config(bg=Alarm.DEFAULT_COLOR)

            time.sleep(Alarm.ALARM_INTERVAL)

class Main(Frame):

    D_FONT = ('돋움',11)
    PADX = 5
    PADY = 5

    WEEKDAY_LIST = ['월','화','수','목','금', '토', '일']

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.add_clock_section()
        
        self.add_alarm_section(Main.WEEKDAY_LIST[datetime.datetime.now().weekday()])
    
    def add_clock_section(self):
        self.clock = Label(self.master, text="", fg="Red", font=("Helvetica", 18))
        self.clock.grid(column=0, row=0)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.clock.configure(text=now)
        self.after(900, self.update_clock)


    def add_alarm_section(self, week_day):        
        self.time_table_dict = loader.load_time_table()

        self.period_dict = loader.load_time_slot()
        print(self.period_dict)

        self.zoom_url_dict = loader.load_subject_urls()
        print(self.zoom_url_dict)

        self.enabled_list = []
        self.add_alarms(week_day)

    
    def add_alarms(self, week_day):

        if week_day not in self.time_table_dict:
            label = Label(self.master, text=f'{week_day}요일 에는 수업이 없습니다.', 
                anchor='w', relief='ridge', width=40, height=2, font=Main.D_FONT)
            label.grid(column=0, row=1, pady=Main.PADY, padx=Main.PADX)
            return

        subject_list = self.time_table_dict[week_day]
        self.enabled_list = [True for i in range(len(subject_list)+2)]

        # 조회
        period = 0
        start_time, end_time, url, cont = self.extract_period_info(period, "조회")
        text = self.make_label_text(0, start_time, end_time, "조회", cont)
        self.create_label_and_button(text, url, period+1, period, start_time)

        # 종례
        period = len(subject_list) + 1
        start_time, end_time, url, cont = self.extract_period_info(period, "종례")
        text = self.make_label_text(period, start_time, end_time, "종례", cont)
        self.create_label_and_button(text, url, period+1, period, start_time)
        
        period = 1
        row = 2
        #            if period == 0:
        #        text = f'조회 {start_time}~{end_time} 조회 ({cont})'
        #    else:

        for subject in subject_list:

            start_time, end_time, url, cont = self.extract_period_info(period, subject)

            text = self.make_label_text(period, start_time, end_time, subject, cont)
            self.create_label_and_button(text, url, row, period, start_time)
            row += 1
            period += 1
            
    def make_label_text(self, period, start_time, end_time, subject, cont):
        return f'{period}교시 {start_time}~{end_time} {subject} ({cont})'

    def extract_period_info(self, period, subject):
        start_time = self.period_dict[f'{period}'][0]
        end_time = self.period_dict[f'{period}'][1]
        if subject in self.zoom_url_dict.keys():
            url = self.zoom_url_dict[subject]
            cont = 'Zoom수업'
        else:
            url = None
            cont = "Contents수업"

        return (start_time, end_time, url, cont)

    def create_label_and_button(self, text, url, row, alarm_index, start_time):
        label = Label(self.master, text=text, 
                anchor='w', relief='ridge', width=40, height=2, font=Main.D_FONT)
        label.grid(column=0, row=row, pady=Main.PADY, padx=Main.PADX)

        alarm = Alarm(label, alarm_index, self.enabled_list, start_time)
        alarm.start()

        btn_stop_alarm = Button(self.master, text='Stop', font=Main.D_FONT,
            width=5, height=2, command = partial(self.clicked_btn_stop_alarm, alarm_index, self.enabled_list))
        btn_stop_alarm.grid(column=1, row=row, pady=Main.PADY, padx=Main.PADX)

        btn_open_zoom = Button(self.master, text='Open', font=Main.D_FONT,
            width=5, height=2, command = partial(self.clicked_btn_open_zoom, url))
        btn_open_zoom.grid(column=2, row=row, pady=Main.PADY, padx=Main.PADX)


    def clicked_btn_stop_alarm(self, index, enabled_list):
        print(f'stop: {index}')
        self.enabled_list[index] = False

    def clicked_btn_open_zoom(self, url):
        webbrowser.open_new_tab(url)


if __name__ == "__main__":
    root = Tk()
    main_frame = Main(root)

    root.wm_title("ClassHelper")
    #root.geometry("800x600")
    root.mainloop()