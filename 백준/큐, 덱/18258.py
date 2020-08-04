import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self): # head에 pop, tail에 push
        self.head = None
        self.tail = None
        self.amount = 0 # 큐에 저장된 node의 갯수를 기록함
        
    def push(self, data):
        newNode = Node(data)
        newNode.next = None
        if self.head == None: # 큐에 아무것도 없는 경우
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.amount += 1
            
    def pop(self):
        if self.head == None: # 큐에 아무것도 없는 경우
            print('-1')
        else:
            res = self.head.data
            self.head = self.head.next
            print(res)
            self.amount -= 1
            
    def size(self):
        print(self.amount)
        
    def empty(self):
        if self.head == None:
            print('1')
        else:
            print('0')
            
    def front(self):
        if self.head == None:
            print('-1')
        else:
            print(self.head.data)
    
    def back(self):
        if self.head == None:
            print('-1')
        else:
            print(self.tail.data)

q = Queue()
for _ in range(int(input())):
    string = sys.stdin.readline().split()
    #string = input().split()
    if string[0] == 'push':
        q.push(string[1])
    elif string[0] == 'pop':
        q.pop()
    elif string[0] == 'size':
        q.size()
    elif string[0] == 'empty':
        q.empty()
    elif string[0] == 'front':
        q.front()
    elif string[0] == 'back':
        q.back()