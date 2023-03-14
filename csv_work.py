import csv

def read_list(csvfile):
    t=[('Room','Capacity','From','To')]
    a=[('Room','Capacity')]
    o=[('Room','From','To')]
    
    with open(csvfile) as f:
        l=list(csv.DictReader(f))
        for row in l:
            _t = row['Room'],row['Capacity'],row['From'],row['To']
            t.append(_t)
            if row['oc'] == '0':
                _a = row['Room'],row['Capacity']
                a.append(_a)
            if row['oc'] == '1':
                _o = row['Room'],row['From'],row['To']
                o.append(_o)
    return t,a,o
    
    

def printit(to_print):
    from tabulate import tabulate
    print(tabulate(to_print,headers="firstrow", tablefmt="grid"))
