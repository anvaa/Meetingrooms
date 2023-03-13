import sys,os
import csv



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
        
        return "er ledig"
    
def _select_av_rooms(self):
    print("  -Available Rooms-")
    t=""
    for r in self.av_rooms:
        _=f"  {r[0]}, {r[1]}"
        t=t+r[0]+" "
        print(_)
    s = input("Select room number: ")
    
    if s in t:
        return int(s)
    return 0
    

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
                o.append(_)
    return t,a,o