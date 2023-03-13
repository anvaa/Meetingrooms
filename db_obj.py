import sqlite3
import sys,os

class Db:
    def __init__(self, dbfile="hotel.db"):
        
        if not check_file(dbfile):
            raise ValueError("No database file found.")
        
        self._dbfile = dbfile
        self._count_occupied = 0
       
    try:
        @property
        def count_occupied(self):
            return count_occupied(self._dbfile)
        
        @property
        def get_occupied(self):
            return list_occupied(self._dbfile)
        
        @property
        def get_not_occupied(self):
            return list_not_occupied(self._dbfile)
        
        
        @property
        def get_room_type(self):
            return list_room_type(self._dbfile)
        
        def __str__(self):
            s=""
            for r in list_not_occupied(self._dbfile):
                s=s + f"{r[0]} {r[1]}\n"
            return f"Free Roomes:\n{s}"
        
        
    except sqlite3.Error as e:    
        sys.exit(e)

def main():
    ...

        
def list_room_type(dbfile):
        sqliteConnection = sqlite3.connect(dbfile)
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT DISTINCT type FROM rooms WHERE oc=0;")
        _ = cursor.fetchall()
        return _
            
        
def count_occupied(dbfile):
        sqliteConnection = sqlite3.connect(dbfile)
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT COUNT(oc) FROM rooms WHERE oc>0;")
        _ = cursor.fetchall()
        return int(_[0][0])
    
def list_occupied(dbfile):
        sqliteConnection = sqlite3.connect(dbfile)
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT nr,fdate,tdate FROM occupied ORDER BY nr;")
        return cursor.fetchall()
    
def list_not_occupied(dbfile):
        sqliteConnection = sqlite3.connect(dbfile)
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT nr,type FROM rooms WHERE oc=0;")
        return cursor.fetchall()

    
def check_file(fname):
    if os.path.isfile(fname):
        return True
    return False




if __name__ == "__main__":
    main()