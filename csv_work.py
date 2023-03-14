import csv

def read_list(csvfile):
    
    t=[]
    a=[]
    o=[]
    with open(csvfile) as f:
        
        for r in consolidate_rooms(csv.DictReader(f)):
            t.append({"Room":r["Room"],"Capacity":r["Capacity"],"From":r["From"],"To":r["To"],"oc":r["oc"]})
            if r["oc"] == "0":
                a.append({"Room":r["Room"],"Capacity":r["Capacity"]})
            if r["oc"] == "1":
                o.append({"Room":r["Room"],"From":r["From"],"To":r["To"]})
    return t,a,o
    

def write_list(csvfile,save_dict):
    
    with open(csvfile,"w") as f:
        header=["Room","Capacity","From","To","oc"]
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        
        for r in save_dict:
            writer.writerow(r)

    
def consolidate_rooms(ro):
    from datetime import datetime
    d = datetime.now().strftime("%Y-%m-%d %H:%m")
    n=[]
    for r in ro:
        if r["To"] == "0":
            n.append({"Room":r["Room"],"Capacity":r["Capacity"],"From":r["From"],"To":r["To"],"oc":r["oc"]})
        else:
            if r["To"] < d:
                r["From"] = 0
                r["To"] = 0
                r["oc"] = 0
                n.append({"Room":r["Room"],"Capacity":r["Capacity"],"From":r["From"],"To":r["To"],"oc":r["oc"]})
            elif r["To"] > d:
                n.append({"Room":r["Room"],"Capacity":r["Capacity"],"From":r["From"],"To":r["To"],"oc":r["oc"]})
                
    return n


def printit(to_print):
    from tabulate import tabulate
    print(tabulate(to_print,headers="keys", tablefmt="grid"))
