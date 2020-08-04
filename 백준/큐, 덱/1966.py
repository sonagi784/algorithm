class Node:
    def __init__(self, data, pri):
        self.data = data
        self.pri = pri
        self.next = None

class Queue:
    def __init__(self):
        self.head = None # pop
        self.tail = None # push
    
    def isempty(self):
        if self.head == None:
            return True
        return False
    
    def getmaxpri(self):
        now = self.head
        maxval = now.pri
        while(now != None):
            if maxval < now.pri:
                maxval = now.pri
            now = now.next
        return maxval
        
    def push(self, data, pri):
        newNode = Node(data, pri)
        if self.isempty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def pop(self):
        if self.isempty():
            raise IndexError('pop from empty Queue')
        else:      
            ret = []
            ret.append(self.head.data)
            ret.append(self.head.pri)
            self.head = self.head.next
            return ret
        
    def peek(self):
        if self.isempty():
            raise IndexError('peek from empty Queue')
        else:
            ret = []
            ret.append(self.head.data)
            ret.append(self.head.pri)
            return ret
    
for _ in range(int(input())):
    N, M = map(int, input().split()) # M: index (0 <= M < N)
    priority = list(map(int, input().split()))
    times = 0
    q = Queue()
    for i in range(N):
        q.push(i, priority[i]) # data : index
    while(1):
        val = q.peek()
        if val[0] == M and val[1] == q.getmaxpri():
            times += 1
            print(times)
            break;
        elif val[1] == q.getmaxpri():
            times += 1
            q.pop()
        else:
            val = q.pop()
            q.push(val[0], val[1])