
def load_subject_urls():
    subject_dict = {}
    with open("subject_zoom_url.txt", "r", encoding="UTF-8") as input:
        while True:
            line = input.readline().strip()
            if not line: 
                break
            subject, zoom_url = line.split(",")
            #print(line)
            #print(subject, zoom_url)
            subject_dict[subject] = zoom_url

    return subject_dict

def load_time_table():
    timetable_dict = {}
    with open("time_table.txt", "r", encoding="UTF-8") as input:
        while True:
            subjects = []
            line = input.readline().strip()
            if not line: 
                break
            tokens = line.split(",")
            week_day = tokens[0]
            subjects = tokens[1:]
            timetable_dict[week_day] = subjects

    return timetable_dict

def load_time_slot():
    timeslot_dict = {}
    with open("time_slot.txt", "r", encoding="UTF-8") as input:
        while True:
            start_end = []
            line = input.readline().strip()
            if not line: 
                break
            tokens = line.split(",")
            period = tokens[0]
            start_end = tokens[1:]
            timeslot_dict[period] = start_end

    return timeslot_dict
