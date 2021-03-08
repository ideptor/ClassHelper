from tkinter import *
import time
import tkinter
from functools import partial
import webbrowser
import time
import threading
import datetime

class Alarm(threading.Thread):

    ALARM_COLOR = 'red'
    DEFAULT_COLOR = 'SystemButtonFace'
    ALARM_INTERVAL = 0.6
    
    ALARM_DURATUIN_SEC = 5 * 60
    

    def __init__(self, label, index, enabled_list, start_time):
        super().__init__()
        self.setDaemon(True)
        self.label = label
        self.index = index
        self.enabled_list = enabled_list
        self.start_hour = int(start_time[0:2])
        self.start_min = int(start_time[3:5])
        print( self.start_hour, self.start_min)
    
    def run(self):
        
        cur_col = Alarm.ALARM_COLOR
        while True:
            if self.enabled_list[self.index] == True:

                #if self.index == 1:
                    #elapsed_sec = int(datetime.datetime.now().timestamp()) % Alarm.DAY_SEC
                    #print(self.start_time_sec, self.end_time_sec, elapsed_sec, datetime.datetime.now())
                now = datetime.datetime.now()
                start = now.replace(hour=self.start_hour, minute=self.start_min, second=0)
                diff_seconds = (now - start).total_seconds()
                
                if diff_seconds < 0 or diff_seconds >= Alarm.ALARM_DURATUIN_SEC:
                    time.sleep(Alarm.ALARM_INTERVAL)
                    continue
                    

                if cur_col == Alarm.ALARM_COLOR:
                    cur_col = Alarm.DEFAULT_COLOR
                else:
                    cur_col = Alarm.ALARM_COLOR
                self.label.config(bg=cur_col)
                #print(f'change {cur_col}')
            else:
                cur_col = Alarm.DEFAULT_COLOR
                self.label.config(bg=cur_col)
            time.sleep(Alarm.ALARM_INTERVAL)

class Main(Frame):

    D_FONT = ('Helvetica',11)
    PADX = 5
    PADY = 5

    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.clock = Label(self.master, text="", fg="Red", font=("Helvetica", 18))
        self.clock.grid(column=0, row=0)
        #self.label.place(x=50,y=80)
        self.update_clock()

        self.enabled_list =  [True for i in range(10)]
        self.add_alarms()

        #self.enabled_list[1] = True
        #self.enabled_list[2] = True
    
    def add_alarms(self):
        
        #enabled_list = [False, True, False, True, False, False, False, False, False]
        offset_row = 0
        for index in range(1,7):
            start_time = f'{16+index}:42'
            url = 'http://www.naver.com'
            label = Label(self.master, text=f' Hello subject {index} / {start_time}', anchor='w',
                relief='ridge', width=20, height=2, font=Main.D_FONT)
            label.grid(column=0, row=offset_row+index, pady=Main.PADY, padx=Main.PADX)
            alarm = Alarm(label, index, self.enabled_list, start_time)
            alarm.start()

            btn_stop_alarm = Button(self.master, text='Stop', font=Main.D_FONT,
                width=5, height=2, command = partial(self.clicked_btn_stop_alarm, index, self.enabled_list))
            btn_stop_alarm.grid(column=1, row=offset_row+index, pady=Main.PADY, padx=Main.PADX)

            btn_open_zoom = Button(self.master, text='Open', font=Main.D_FONT,
                width=5, height=2, command = partial(self.clicked_btn_open_zoom, url))
            btn_open_zoom.grid(column=2, row=offset_row+index, pady=Main.PADY, padx=Main.PADX)
            

    def clicked_btn_stop_alarm(self, index, enabled_list):
        print(f'stop: {index}')
        self.enabled_list[index] = False

    def clicked_btn_open_zoom(self, url):
        webbrowser.open_new_tab(url)

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.clock.configure(text=now)
        self.after(1000, self.update_clock)


if __name__ == "__main__":
    root = Tk()
    main_frame = Main(root)

    root.wm_title("ClassHelper")
    root.geometry("800x600")
    root.mainloop()