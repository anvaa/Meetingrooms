import sys
from csv_work import printit
from rooms import Rooms

def main():

    try:
        start_menu()
            
    except ValueError as e:
        sys.exit(e)
    
def start_menu():
    while True:
        print(f"\n-Meeting Room Booking-\n[1] New Booking\n[2] Available Rooms\n[3] Occupied Rooms\n[4] View all rooms\n[5] Save & Exit")
        try:
            i = int(input("Select Action: ").strip())
        except:
            i=0

        R=Rooms()
        if i == 1:
            R.new_room()
        
        elif i == 2:
            print(f"\n -Available rooms-")
            printit(R.av_rooms)
            
        elif i == 3:
            print(f"\n -Occupied rooms-")
            printit(R.oc_rooms)
            
        elif i == 4:
            print(f"\n -All rooms-")
            printit(R.all_rooms)
            
        elif i == 5:
            sys.exit("Room Booking Saved.")
        
        elif i == 0:
            print(f"\n<< Nothing selected >>")    
            
        else:
            print(f"\n<< Invalid selection >>")

if __name__ == "__main__":
    main()