import sys
from csv_work import Rooms

def main():

    try:
        print(f"  -Start menu-\n  [1] New Booking\n  [2] List Available Rooms\n  [3] List Occupied Rooms")
        i = int(input("Select Action: "))

        R=Rooms()
        if i == 1:
            R.new_room()
        
        if i == 2:
            print("  -Available rooms-")
            for r in R.av_rooms:
                print(f"  {r[0]} - {r[1]}")
        
        if i == 3:
            print("  -Occupied rooms-")
            for r in R.oc_rooms:
                print(f"  {r[0]} - {r[1]}")
            
    except ValueError as e:
        sys.exit(e)
    
    

if __name__ == "__main__":
    main()