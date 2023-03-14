import sys,os
from csv_work import read_list, printit
from datetime import datetime

class Rooms:
    def __init__(self,csvfile="meeting_rooms.csv"):
        
        if not os.path.isfile(csvfile):
            sys.exit(f"{csvfile} don´t exists.")

        self.all_rooms,self.av_rooms,self.oc_rooms = read_list(csvfile)

    def new_room(self):
        r=_select_av_rooms(self.all_rooms)
        if r == 0:
            raise ValueError(f"Room is not available.")


    
def _select_av_rooms(all_rooms):
    print(f"\n-New Room-")
    
    fd = is_date(input("From Date: ").strip())
    td = is_date(input("To Date: ").strip())
    
    rooms,t = find_available_rooms(all_rooms,fd,td)
    
    print(f"\n-Available Rooms-")
    printit(rooms)
    
    nr = input(f"Select Room Number: ").strip()
    if nr in t:
        print("correct")
    else:
        print("Fail")
        # TODO "set room as oc"
    
    return 0

def find_available_rooms(ro,fd,td):
    t=""
    n=[{"Room","Capacity"}]
    for r in ro:
        print(r)
        # if r[2] > fd:
        #     if r[3] < td:
        #         _=r[0],r[1]
        #         n.append(_)
        #         t=t+r[0]+" "
    return n, t


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


