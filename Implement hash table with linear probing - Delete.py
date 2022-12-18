def delete(self,value):
    key = value % self.Size
    index = key
    while(self.arr[index] != value):
        index = (index + 1) % self.SIZE
        if index == key:
            return 0
    self.arr[index] = -1
    return 1