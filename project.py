import sys
from db_obj import Db
from rooms_obj import Rooms

def main():

    try:
        R=Rooms()
    except ValueError as e:
        sys.exit(e)
    
    
    
    
    print(R.room_type)
    
    
         










if __name__ == "__main__":
    main()