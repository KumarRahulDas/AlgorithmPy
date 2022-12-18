class HashTable:
    def __init__(self,size):
        self.SIZE = size
        self.arr = [None] * self.SIZE
        for i in range(self.SIZE):
            self.arr = -1

    def insert(self,value):
        key = value % self.SIZE
        index = key
        while(self.arr[index] != -1):
            index = (index + 1) % self.SIZE
            if index == key:
                print("Hash Table Is Full")
                return 0
        self.arr[index] = value
        return 1