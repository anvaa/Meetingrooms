import sys,os
from csv_work import read_list, write_list, sort_rooms, printit
from datetime import datetime

class Rooms:
    def __init__(self,csvfile="meeting_rooms.csv"):
        
        if not os.path.isfile(csvfile):
            raise FileNotFoundError(f"{csvfile} don´t exists.")

        self.csvfile=csvfile
        self.all_rooms,self.av_rooms,self.oc_rooms = read_list(self.csvfile)
        
    def new_room(self):
        nr,fd,td,oc=_select_av_rooms(self.all_rooms)
        # 2023-03-15 11:00
        for ro in self.all_rooms:
            if ro["Room"] == nr:
                ro["From"] = fd
                ro["To"] = td
                ro["oc"] = oc

        write_list(self.csvfile, self.all_rooms)

    def remove_rooms(self):
        nr = _deselect_av_rooms(self.oc_rooms)
        for ro in self.all_rooms:
            if ro["Room"] == nr:
                ro["From"] = 0
                ro["To"] = 0
                ro["oc"] = 0

        write_list(self.csvfile, self.all_rooms)

    
    def save_rooms(self):
        write_list(self.csvfile, self.all_rooms)
        
        
def _select_av_rooms(all_rooms):
    print(f"\n-New Room-")
    
    fd = is_date(input("From Date: ").strip())
    td = is_date(input("To Date: ").strip())
    
    rooms,t = find_available_rooms(all_rooms,fd,td)
    
    print(f"\n-Available Rooms-")
    printit(rooms)
    
    nr = input(f"Select Room Number: ").strip()
    
    if nr in t:
        return nr,fd,td,1
    else:
        raise ValueError(f"Room number not in list.")
    

def find_available_rooms(ro,fd,td):
    t=""
    n=[]
    for r in ro:
        if r["From"] == "0":
            n.append({"Room":r["Room"],"Capacity":r["Capacity"]})
            t=t+r["Room"]+" "
        else:
            if r["From"] < fd:
                if r["To"] > td:
                    n.append({"Room":r["Room"],"Capacity":r["Capacity"]})
                    t=t+r["Room"]+" "
    return n, t


def _deselect_av_rooms(oc_rooms):
    print(f"\n-Occupied Rooms-")
    
    rooms=find_occupied_room_nr(oc_rooms)
    printit(oc_rooms)
    
    nr = input(f"Select Room Number: ").strip()
    if nr in rooms:
        return nr
    else:
        raise ValueError(f"Room number not in list.")
 
def find_occupied_room_nr(ro):   
    o=""
    for r in ro:
        o=o+r["Room"]+ " "
    return o


def is_date(dt):
    try:
        da,ti = dt.split(" ")
        y,mo,d = da.split("-")
        h,mi = ti.split(":")
        
        valid_date = f"{y}-{mo}-{d} {h}:{mi}:00"
        
    except: 
        raise ValueError("Wrong date/time format. Try yyyy-mm-dd hh:mm")
    
    validate_date_time(valid_date)
    
    return valid_date

def validate_date_time(test_date=""):
    d = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if test_date < d:
        raise ValueError("Date is in the past.")
    return True