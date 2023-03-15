import sys
from csv_work import printit, write_list
from rooms import Rooms

def main():

    try:
        start_menu()
            
    except ValueError as e:
        sys.exit(e)
    
def start_menu():
    while True:
        print(f"\n-Meeting Room Booking-\n[1] New Booking\n[2] Remove Booking\n[3] Available Rooms\n[4] Occupied Rooms\n[5] All Rooms\n[6] Save & Exit")
        try:
            i = int(input("Select Action: ").strip())
        except:
            i=0

        R=Rooms()
        if i == 1:
            R.new_room()
        
        elif i == 2:
            R.remove_rooms()
            
        elif i == 3:
            print(f"\n-Available rooms-")
            printit(R.av_rooms)
            
        elif i == 4:
            print(f"\n-Occupied rooms-")
            printit(R.oc_rooms)
            
        elif i == 5:
            print(f"\n-All rooms-")
            printit(R.all_rooms)
            
        elif i == 6:
            R.save_rooms()
            sys.exit("Room Booking Saved.")
        
        elif i == 0:
            print(f"\n<< Nothing selected >>")    
            
        else:
            print(f"\n<< Invalid selection >>")



if __name__ == "__main__":
    main()