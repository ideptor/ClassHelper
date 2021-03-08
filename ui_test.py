# https://076923.github.io/posts/Python-tkinter-1/
import tkinter
from functools import partial
import webbrowser

def click_btn_open(url):
    webbrowser.open_new_tab(url)


def init():
    window = tkinter.Tk()

    window.title('Hello')
    #window.geometry('1024x800+100+100')
    window.geometry('640x480')
    window.resizable(False, False)

    label = tkinter.Label(window, text="hello")
    label.grid(column=0, row=0)
    #label.pack()
    url = 'www.naver.com'
    btn_open = tkinter.Button(window, text='open', 
        command=partial(click_btn_open, url))
    btn_open.grid(column=1, row=0)

    window.mainloop()

if __name__ == '__main__':
    init()