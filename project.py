import sys
from dbwork import Db

def main():

    try:
        ... #DB=Db()
    except ValueError as e:
        sys.exit(e)
    
    
    print(Db())
    
    
         










if __name__ == "__main__":
    main()