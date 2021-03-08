# https://076923.github.io/posts/Python-tkinter-1/
import tkinter
from functools import partial
import webbrowser
import time
import threading

def click_btn_open(url):
    webbrowser.open_new_tab(url)


#label2 = None

"""
def alarm(label):
    while True:
        label2.config(bg='red')
        print('change red')
        time.sleep(1)
        label2.config(bg='white')
        time.sleep(1)
        print('change white')
"""

class Alarm(threading.Thread):
    def __init__(self, label):
        super().__init__()
        self.label = label
    
    def run(self):
        while True:
            self.label.config(bg='red')
            print('change red')
            time.sleep(1)
            self.label.config(bg='white')
            time.sleep(1)
            print('change white')  

def init():
    #global label2
    window = tkinter.Tk()

    window.title('Hello')
    #window.geometry('1024x800+100+100')
    window.geometry('640x480')
    window.resizable(False, False)

    label1 = tkinter.Label(window, bg='blue', text="hello", 
        font=('Times', '17'))
    label1.grid(column=0, row=0)
    #label.pack()

    label2 = tkinter.Label(window, text="hello")
    label2.grid(column=1, row=0, padx = 20)
    label2.config(bg = 'red')

    url = 'www.naver.com'
    btn_open = tkinter.Button(window, text='open', width=20, 
         font=(None, '14'), command=partial(click_btn_open, url))
    btn_open.grid(column=2, row=0)

    label3 = tkinter.Label(window, text="hello")
    label3.grid(column=0, row=1, pady=10)

    
    label4 = tkinter.Label(window, text="hello")
    label4.grid(column=0, row=2)

    label5 = tkinter.Label(window, text="hello")
    label5.grid(column=0, row=3, pady=50)

    #time.sleep(5)
    t = Alarm(label2)
    t.start()

    window.mainloop()


if __name__ == '__main__':
    init()
