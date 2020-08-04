class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class Stack: 
    def __init__(self): 
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.head == None:
            print('-1')
            return;
        print(self.head.data)
        self.head = self.head.next

    def size(self):
        result = 0
        temp = self.head
        while(self.head != None):
            result += 1
            self.head = self.head.next
        print(result)
        self.head = temp

    def empty(self):
        print(1 if self.head == None else 0)

    def top(self):
        print(-1 if self.head == None else self.head.data)

import sys

s = Stack() 
for _ in range(int(input())): 
    command = sys.stdin.readline()
    command = command.split()
    if len(command) == 2: 
        cmd = 's.' + command[0] + '(' + command[1] + ')' 
    else: 
        cmd = 's.' + command[0] + '(' + ')' 
    exec(cmd)