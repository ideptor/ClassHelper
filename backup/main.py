import tkinter as tk
import subject_zoom_url_loader as loader

win = tk.Tk()
dict_sub_zoom_del = {}


tf_zoom_url = None
tf_subject = None


def click_btn_add():
    add_subject_zoom_url_record(tf_subject.get(), tf_zoom_url.get())

def click_btn_del():
    pass


def subject_add():
    global tf_zoom_url
    global tf_subject

    tk.Label(win, text="Subject:",).grid(column=0, row=0)

    subject = tk.StringVar()
    tf_subject = tk.Entry(win, width=12, textvariable=subject)
    tf_subject.grid(column=1,row=0)

    tk.Label(win, text="zoomURL:",).grid(column=2, row=0)
    
    zoom_url = tk.StringVar()
    tf_zoom_url = tk.Entry(win, width=30, textvariable=zoom_url)
    tf_zoom_url.grid(column=3,row=0)

    btn_add_subject_zoom = tk.Button(win, text="Add", command=click_btn_add).grid(column=4,row=0)


def init():
    global cur_row 

    subject_dict = loader.load_subject_urls()
    for subject, zoom_url in subject_dict.items():
        cur_row += 1
        #print(f"{subject}: {zoom_url}")
        tk.Label(win, text=f"{subject}").grid(column=0, row=cur_row)
        tk.Label(win, text=f"{zoom_url}").grid(column=1, row=cur_row)
        btn_del_subject_zoom = tk.Button(win, text="del", command=click_btn_del).grid(column=2,row=cur_row)    



cur_row = 0

def add_subject_zoom_url_record(subject, zoom_url):
    global cur_row 
    
    cur_row += 1
    print(f"{subject}: {zoom_url}")
    tk.Label(win, text=f"{subject}").grid(column=0, row=cur_row)
    tk.Label(win, text=f"{zoom_url}").grid(column=1, row=cur_row)
    btn_del_subject_zoom = tk.Button(win, text="del", command=click_btn_del).grid(column=2,row=cur_row)    

    row_list = []


#window setting
win.title("Class Helper")
win.resizable(False, False)
init()

win.mainloop()