import sys,os
import csv,re

class Rooms:
    def __init__(self,csvfile="hotel.csv"):
        
        if not os.path.isfile(csvfile):
            sys.exit(f"{csvfile} don´t excists.")

        self.all_rooms = read_list(csvfile)[0]
        self.av_rooms = read_list(csvfile)[1]
        self.oc_rooms = read_list(csvfile)[2]

    def new_room(self):
        r=_select_av_rooms(self)
        if r == 0:
            raise ValueError(f"Room is not available.")
        
       
    
def _select_av_rooms(self):
    
    fd = is_date(input("From Date: ").strip())
    td = is_date(input("To Date: ").strip())
    validate_dates(fd,td)
    
    print(f"\n-Available Rooms-")
    t=""
    for r in self.av_rooms:
        _=f"{r[0]}, {r[1]}"
        t=t+r[0]+" "
        print(_)
    nr = input(f"\nSelect room number: ").strip()
    if nr in t:
        ...
    
    
    return 0

def validate_dates(fd,td):
    


def is_date(dt):
    try:
        y,m,d = dt.split("-")
    except: 
        raise ValueError("Wrong date format.") 


def read_list(csvfile):
    t=[]
    a=[]
    o=[]
    with open(csvfile) as f:
        d = csv.DictReader(f)
        for r in d:
            _ = r["nr"],r["type"]
            t.append(_)
            if r["oc"] == "0":
                a.append(_)
            if r["oc"] == "1":
                __ = r["nr"],r["type"],r["fdate"],r["tdate"]
                o.append(__)
    return t,a,o