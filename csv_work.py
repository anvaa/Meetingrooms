import sys,os
import csv
from datetime import datetime

class Rooms:
    def __init__(self,csvfile="meeting_rooms.csv"):
        
        if not os.path.isfile(csvfile):
            sys.exit(f"{csvfile} don´t excists.")

        self.all_rooms = read_list(csvfile)[0]
        self.av_rooms = read_list(csvfile)[1]
        self.oc_rooms = read_list(csvfile)[2]

    def new_room(self):
        r=_select_av_rooms(self.all_rooms)
        if r == 0:
            raise ValueError(f"Room is not available.")


    
def _select_av_rooms(all_rooms):
    print(f"\n-New Room-")
    fd = is_date(input("From Date: ").strip())
    td = is_date(input("To Date: ").strip())
    
    
    print(f"\n-Available Rooms-")
    t=""
    for r in all_rooms:
        _=f"{r[0]}, {r[1]}"
        t=t+r[0]+" "
        print(_)
    nr = input(f"\nSelect room number: ").strip()
    if nr in t:
        ...
        # TODO "set room as oc"
    
    
    return 0


def is_date(dt):
    try:
        da,ti = dt.split(" ")
        y,mo,d = da.split("-")
        h,mi = ti.split(":")
        
        valid_date = f"{y}-{mo}-{d} {h}:{mi}"
        validate_date_time(valid_date)
    except: 
        raise ValueError("Wrong date/time format. Try yyyy-mm-dd hh:mm")
    return valid_date

def validate_date_time(test_date):
    d = datetime.now().strftime("%Y-%m-%d %H:%m")
    if test_date < d:
        raise ValueError("Date is in the past.")
    return True




def read_list(csvfile):
    t=[]
    a=[]
    o=[]
    with open(csvfile) as f:
        d = csv.DictReader(f)
        for r in d:
            _t = r["nr"],r["seats"],r["fdate"],r["tdate"],r["oc"]
            t.append(_t)
            if r["oc"] == "0":
                _a = r["nr"],r["seats"]
                a.append(_a)
            if r["oc"] == "1":
                _o = r["nr"],r["fdate"],r["tdate"]
                o.append(_o)
    return t,a,o