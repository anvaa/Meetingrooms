from dbwork import Db

class Room:
    def __init__(self,capacity=10):
        
        DB = Db()
        self.capasity = capacity
        
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(salf,value):
        if value >= 0:
            self._capacity = value
        else: raise ValueError("Negative capacity")