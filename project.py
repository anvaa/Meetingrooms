import sys
from csv_work import Rooms

def main():

    try:
        start_menu()
            
    except ValueError as e:
        sys.exit(e)
    
def start_menu():
    while True:
        print(f"\n-Meeting Room Booking-\n[1] New Booking\n[2] Available Rooms\n[3] Occupied Rooms\n[4] Exit Program")
        try:
            i = int(input("Select Action: ").strip())
        except:
            i=0

        R=Rooms()
        if i == 1:
            R.new_room()
        
        elif i == 2:
            print(f"\n-Available rooms-")
            for r in R.av_rooms:
                print(f"{r[0]} - {r[1]} seats")
        
        elif i == 3:
            print(f"\n-Occupied rooms-")
            for r in R.oc_rooms:
                print(f"{r[0]} - {r[1]} > {r[2]}")   

        elif i == 4:
            sys.exit("bye bye")
        
        elif i == 0:
            print(f"\n<< Nothing selected >>")    
            
        else:
            print(f"\n<< Invalid selection >>")

if __name__ == "__main__":
    main()