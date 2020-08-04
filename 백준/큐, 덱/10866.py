class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class Deque:
    def __init__(self):
        self.head = None # front
        self.tail = None # back
        
    def isempty(self):
        if self.head == self.tail == None:
            return True
        return False
    
    def push_front(self, data):
        newNode = Node(data)
        if self.isempty():
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
    
    def push_back(self, data):
        newNode = Node(data)
        if self.isempty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            
    def pop_front(self):
        if self.isempty(): # 0
            ret_data = -1
        elif self.head == self.tail: # 1
            ret_data = self.head.data
            self.head = None
            self.tail = None
        else: # 2 이상
            ret_data = self.head.data
            self.head = self.head.next
            self.head.prev = None
        print(ret_data)
        
    def pop_back(self):
        if self.isempty(): # 0
            ret_data = -1
        elif self.head == self.tail: # 1
            ret_data = self.tail.data
            self.head = None
            self.tail = None
        else: # 2 이상
            ret_data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        print(ret_data)
    
    def size(self):
        count = 0
        temp = self.head
        while(temp != None):
            count += 1
            temp = temp.next
        print(count)
        
    def empty(self):
        if self.isempty():
            print('1')
        else:
            print('0')
    
    def front(self):
        if self.isempty():
            ret_data = -1
        else:
            ret_data = self.head.data
        print(ret_data)
        
    def back(self):
        if self.isempty():
            ret_data = -1
        else:
            ret_data = self.tail.data
        print(ret_data)

import sys
dq = Deque()
for _ in range(int(input())):
    string = sys.stdin.readline().split()
    cmd = 'dq.' + string[0]
    if len(string) == 1:
        cmd += '()'
    else:
        cmd += '(' + string[1] + ')'
    exec(cmd)