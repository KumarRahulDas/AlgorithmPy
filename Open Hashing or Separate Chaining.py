class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class HashTableChaining:
    def __init__(self):
        self.SIZE = 7
        self.chain = [None] * self.SIZE
    def insert(self,value):
        newNode = Node(value)
        key = value % self.SIZE
        if self.chain[key] == None:
            self.chain[key] = newNode
        else:
            temp = self.chain[key]
            while temp.next != None:
                temp = temp.next
            temp.next = newNode;