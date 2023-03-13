import sys



class Rooms:
    def __init__(self, value=10):
        
        
        self.capacity = int(value)
        self.free_rooms = get_not_occupied()
        self.occupied_rooms = get_occupied()
        self.room_type = get_room_type()
        
        
        @property
        def capacity(self):
            return self._capacity
        
        @capacity.setter
        def capacity(self, n):
            if not n >= 0:
                raise ValueError("Negative capacity")
            else:
                self._capacity = n
             
                
        @property
        def free_rooms(self):
            return self._free_rooms
        
        @free_rooms.setter
        def free_rooms(self, v):
            if not v:
                raise ValueError("No data from database")
            self._free_rooms = v
        
        
        @property    
        def room_type(self):
            return self._room_type
        
        @room_type.setter    
        def room_type(self, v):
            if not v:
                raise ValueError("No data from database")
            self._room_type = v

def main():
    ...

def get_not_occupied():
    D=Db()
    return D.get_not_occupied

def get_occupied():
    D=Db()
    return D.get_occupied

def get_room_type():
    D=Db()
    return D.get_room_type




if __name__ == "__main__":
    main()