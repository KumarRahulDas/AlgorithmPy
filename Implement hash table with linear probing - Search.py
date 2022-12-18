def search(self,value):
    key = value % self.SIZE
    index = key
    while(self.arr[index] != value):
        index = (index +1) % self.SIZE
        if index == key:
            return 0
    return 1