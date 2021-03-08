import tkinter as tk
import data_loader as loader

def click_btn_start():
    pass

def click_btn_cancel():
    pass


def init_layout(week_day):
    
    time_table_dict = loader.load_time_table()
    
    subject_list = time_table_dict[week_day]
    print(subject_list)

    period_dict = loader.load_time_slot()
    print(period_dict)

    zoom_url_dict = loader.load_subject_urls()
    print(zoom_url_dict)

    period = 0
    for subject in subject_list:
        period += 1
        start = period_dict[f'{period}'][0]
        end = period_dict[f'{period}'][1]
        if subject in zoom_url_dict.keys():
            url = zoom_url_dict[subject]
            cont = 'Zoom수업'
        else:
            url = None
            cont = "Contents수업"
        tk.Label(win, text=f'{period}교시 {start}~{end} {subject} {cont}').grid(column=0, row=period-1)
        btn_start = tk.Button(win, text="Start", command=click_btn_start).grid(column=1,row=period-1)    
        btn_cancel = tk.Button(win, text="Cancel", command=click_btn_cancel).grid(column=2,row=period-1)    

        #print(f'{period}교시 | {start}~{end} | {subject} | {cont} | {url}')
        




   

#if __name__ == "__main__":
win = tk.Tk()
win.title('class helper')

init_layout("월")
win.mainloop()