class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.amount = 0
    
    def isempty(self):
        if self.head == None:
            return True
        return False
    
    def enqueue(self, data):
        newNode = Node(data)
        if self.isempty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.amount += 1
            
    def dequeue(self):
        if self.isempty():
            raise IndexError('pop from empty queue')
            return;
        ret_data = self.head.data
        self.head = self.head.next
        self.amount -= 1
        return ret_data
    
N = int(input())
if N == 1: 
    print('1')
else:
    q = Queue()
    for n in range(1, N+1): # O(N)
        q.enqueue(n)
    # (2N-3)회  > 삭제 (N-1)회, 옮기기 (N-2)회
    for _ in range(0, N-2): # 삭제+옮기기 N-2 회 반복
        q.dequeue()
        q.enqueue(q.dequeue())
    q.dequeue() # 삭제 1회
    print(q.dequeue())