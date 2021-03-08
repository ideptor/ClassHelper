import data_loader as loader

def test_load_urls():
    ret = loader.load_subject_urls()
    print(ret)

def test_load_time_table():
    ret = loader.load_time_table()
    print(ret)

def test_load_time_slot():
    ret = loader.load_time_slot()
    print(ret)

def test_code_for_init_layout(week_day):
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

        print(f'{period}교시 | {start}~{end} | {subject} | {cont} | {url}')
        


if __name__ == "__main__":
    #test_load_urls()
    #test_load_time_table()
    #test_load_time_slot()
    test_code_for_init_layout("월")